from aiogram import types, Dispatcher
from config import bot, MEDIA_DEST
from database import bot_db
from const import START_MSG, START_GROUP_MSG
from keyboards.start_menu import start_menu_key #start_group_key


async def start_menu(message: types.Message):
    db = bot_db.Database()
    db.sql_insert_all_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

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
