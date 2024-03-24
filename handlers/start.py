import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot, MEDIA_DEST
from database import bot_db
from const import START_MSG, START_GROUP_MSG
from keyboards.start_menu import start_menu_key  # start_group_key


async def start_menu(message: types.Message):
    db = bot_db.Database()
    db.sql_insert_all_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    command = message.get_full_command()
    if command[1] != '':
        link = await _create_link('start', payload=command[1])
        owner = db.select_user_by_link(link=link)

        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text=f'You can not use link!'
            )
            return
        try:
            db.insert_reference_user(
                owner=owner['telegram_id'],
                reference=message.from_user.id
            )
            db.update_owner_balance(
                telegram_id=owner['telegram_id']
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
