from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link
from config import bot
from database.bot_db import Database
from keyboards.reference import reference_menu_key
import const
import binascii
import os


async def reference_menu_call(call: types.CallbackQuery):
    db = Database()
    user_info = db.select_reference_user_info(telegram_id=call.from_user.id)
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text=const.REFERENCE_MENU_MSG.format(
            user=call.from_user.first_name,
            balance=user_info["balance"],
            count=user_info["count"]
        ),
        reply_markup=await reference_menu_key()
    )


# async def list_users_call(call: types.CallbackQuery):
#     db = Database()
#     user_info = db.select_user_list_info(telegram_id=call.from_user.id)
#     print(user_info)
#     # await call.message.delete()
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text=const.LIST_USERS_MSG.format(
#             first_name=user_info["first_name"]
#         ),
#         # reply_markup=await reference_menu_key()
#     )

async def list_users_call(call: types.CallbackQuery):
    db = Database()
    user_info = db.select_user_list_info(telegram_id=call.from_user.id)

    if user_info:
        first_names = [f"{i + 1}) {user['first_name']}" for i, user in enumerate(user_info)]
        first_names_str = '\n'.join(first_names)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=const.LIST_USERS_MSG.format(first_name=first_names_str)
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You are not a referral of any user."
        )


async def reference_link_call(call: types.CallbackQuery):
    db = Database()
    user = db.select_user(telegram_id=call.from_user.id)
    # print(user)
    if user['link']:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'your link {user["link"]}'
        )
    else:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link('start', payload=token)
        db.update_user_link(link=link, telegram_id=call.from_user.id)
        # print(link)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f'your new link is {link}'
        )


def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reference_menu_call,
        lambda call: call.data == 'reference_menu'
    )
    dp.register_callback_query_handler(
        reference_link_call,
        lambda call: call.data == 'reference_link'
    )
    dp.register_callback_query_handler(
        list_users_call,
        lambda call: call.data == 'List_of_users'
    )
