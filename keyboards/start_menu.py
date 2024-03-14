from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_key():
    markup = InlineKeyboardMarkup()

    questionnaire_button = InlineKeyboardButton('Какой ваш любимый цвет?', callback_data='star_questionnaire')
    markup.add(questionnaire_button)
    return markup
