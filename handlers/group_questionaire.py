from aiogram import types, Dispatcher
from config import bot, MEDIA_DEST
from database import bot_db
from const import START_GROUP_MSG
from keyboards.start_menu import start_menu_key  # start_group_key


async def group_start_menu(message: types.Message):
    db = bot_db.Database()
    db.sql_insert_all_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    with open(MEDIA_DEST + 'logo.gif', 'rb') as logo:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=logo,
            caption=START_GROUP_MSG.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_menu_key()
        )


async def ban_call(call: types.CallbackQuery):
    await call.message.delete()
    db = bot_db.Database()
    user_info = db.select_ban_user(call.from_user.id)
    print(user_info)
    if user_info:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'Ваш счетчик банов: {user_info["count"]}'
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Информация о вашем бане не найдена в базе данных.'
        )


def register_group_start_handlers(dp: Dispatcher):
    dp.register_message_handler(
        group_start_menu,
        commands=['start']
    )
    dp.register_callback_query_handler(
        ban_call,
        lambda call: call.data == 'ban_check'
    )
