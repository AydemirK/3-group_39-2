from aiogram import types, Dispatcher
from config import bot
from keyboards.quest import quest_keyboard


async def questionaire_start_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Какой ваш любимый цвет?',
        reply_markup=await quest_keyboard()
    )


async def blue_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Хорошо'
    )


async def red_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='класный цвет'
    )


async def green_call(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(
        chat_id=call.from_user.id,
        text='спасибо'
    )




def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        questionaire_start_call,
        lambda call: call.data == 'star_questionnaire'
    )
    dp.register_callback_query_handler(
        blue_call,
        lambda call: call.data == 'blue'
    )
    dp.register_callback_query_handler(
        red_call,
        lambda call: call.data == 'red'
    )
    dp.register_callback_query_handler(
        green_call,
        lambda call: call.data == 'green'
    )

