import re

from aiogram import types, Dispatcher

import const
from config import bot
from keyboards.profile import profile_key, my_profile_key
from database.bot_db import Database
import random


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.select_profile(telegram_id=call.from_user.id)
    if profile:
        with open(profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_MSG.format(
                    nickname=profile['nickname'],
                    hobby=profile['hobby'],
                    age=profile['age'],
                    married=profile['married'],
                    city=profile['city'],
                    email_address=profile['email_address'],
                    floor=profile['floor']
                ),
                reply_markup=await my_profile_key()
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='You have not registered'
        )


async def delete_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.delete_profile(telegram_id=call.from_user.id)
    # print(profile)


async def ran_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.select_profiles(telegram_id=call.from_user.id)
    if profile:
        random_profile = random.choice(profile)

        with open(random_profile['photo'], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=const.PROFILE_MSG.format(
                    nickname=random_profile['nickname'],
                    hobby=random_profile['hobby'],
                    age=random_profile['age'],
                    married=random_profile['married'],
                    city=random_profile['city'],
                    email_address=random_profile['email_address'],
                    floor=random_profile['floor']
                ),
                reply_markup=await profile_key(telegram_id=random_profile['telegram_id'])
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='liked all profiles'
        )


async def detect_like_call(call: types.CallbackQuery):
    await call.message.delete()
    db = Database()
    own = re.sub('like_', '', call.data)
    db.insert_like_profile(
        owner=own,
        liker=call.from_user.id
    )
    await ran_profile_call(call=call)


async def detect_dislike_call(call: types.CallbackQuery):
    await call.message.delete()
    db = Database()
    own = re.sub('dislike', '', call.data)
    db.insert_dislike_profile(
        owner=own,
        liker=call.from_user.id
    )
    await ran_profile_call(call=call)


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        ran_profile_call,
        lambda call: call.data == 'random_profile'
    )
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == 'my_profile'
    )
    dp.register_callback_query_handler(
        delete_profile_call,
        lambda call: call.data == 'delete_profile'
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: "like_" in call.data
    )
    dp.register_callback_query_handler(
        detect_dislike_call,
        lambda call: "dislike" in call.data
    )
