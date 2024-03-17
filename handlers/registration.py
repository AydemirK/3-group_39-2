import sqlite3
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from config import bot, MEDIA_DEST
from database import bot_db
import const


class RegistrationStates(StatesGroup):
    nickname = State()
    hobby = State()
    age = State()
    married = State()
    city = State()
    email_address = State()
    floor = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Please write your nickname!!!'
    )
    await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="what's your hobby"
    )
    await RegistrationStates.next()


async def load_hobby(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old are you?\n'
             'Just write the numbers.\n'
             "If you don't want to give your age, you can skip it by typing in - "
    )
    await RegistrationStates.next()


async def load_age(message: types.Message, state: FSMContext):
    if message.text == '-':
        pass
    else:
        try:
            int(message.text)
        except ValueError:
            await bot.send_message(
                chat_id=message.from_user.id,
                text='Only NUMBERS\n\n'
                     'Registration failed\n'
                     'Restart process'
            )
            await state.finish()
            return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="marital status (Yes / No)\n"
             "If you don't want to give your status, you can skip it by typing in - "
    )
    await RegistrationStates.next()


async def load_married(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['married'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What city are you from?\n'
    )
    await RegistrationStates.next()


async def load_cty(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='email_address?'
    )
    await RegistrationStates.next()


async def load_email_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email_address'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Floor?\n'
             'male/female or -'

    )
    await RegistrationStates.next()


async def load_floor(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['floor'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Upload a photo'

    )
    await RegistrationStates.next()


async def load_photo(message: types.Message, state: FSMContext):
    db = bot_db.Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DEST
    )
    async with state.proxy() as data:
        db.insert_profile(
            telegram_id=message.from_user.id,
            nickname=data['nickname'],
            hobby=data['hobby'],
            age=data['age'],
            married=data['married'],
            city=data['city'],
            email_address=data['email_address'],
            floor=data['floor'],
            photo=path.name
        )
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=const.PROFILE_MSG.format(
                    nickname=data['nickname'],
                    hobby=data['hobby'],
                    age=data['age'],
                    married=data['married'],
                    city=data['city'],
                    email_address=data['email_address'],
                    floor=data['floor']
                )
            )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'You have successfully Registered 🎆'
    )
    await state.finish()


def register_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == 'registration'
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_hobby,
        state=RegistrationStates.hobby,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_married,
        state=RegistrationStates.married,
        content_types=['text']
    )
    dp.register_message_handler(
        load_cty,
        state=RegistrationStates.city,
        content_types=['text']
    )
    dp.register_message_handler(
        load_email_address,
        state=RegistrationStates.email_address,
        content_types=['text']
    )
    dp.register_message_handler(
        load_floor,
        state=RegistrationStates.floor,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
