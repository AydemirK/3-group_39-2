import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot, MEDIA_DEST
from database import bot_db, sql_queries
from const import START_MSG, START_GROUP_MSG
from keyboards.start_menu import start_menu_key  # start_group_key
from database.async_database import AsyncDatabase


async def start_menu(message: types.Message):
    db = AsyncDatabase()
    await db.execute_query(
        query=sql_queries.INSERT_USER_QUERY,
        params=(
            None,
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
            None,
            0
        ),
        fetch="none"
    )
    command = message.get_full_command()
    if command[1] != '':
        link = await _create_link('start', payload=command[1])
        owner = await db.execute_query(
            query=sql_queries.SELECT_USER_BY_LINK_QUERY,
            params=(link,),
            fetch="one"
        )

        if owner['TELEGRAM_ID'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text=f'You can not use link!'
            )
            return
        try:
            await db.execute_query(
                query=sql_queries.UPDATE_USER_BALANCE_QUERY,
                params=owner["TELEGRAM_ID"],
                fetch="none"
            )

        except sqlite3.IntegrityError:
            await bot.send_message(
                chat_id=message.from_user.id,
                text=f'You have used this link'
            )
            return

    with open(MEDIA_DEST + 'logo.gif', 'rb') as logo:
        await bot.send_animation(
            chat_id=message.chat.id,
            animation=logo,
            caption=START_MSG.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_menu_key()
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_menu,
        commands=['start']
    )
