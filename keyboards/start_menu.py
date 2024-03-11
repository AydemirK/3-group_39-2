from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_key():
    markup = InlineKeyboardMarkup()

    questionnaire_button = InlineKeyboardButton('Опрос про цветов', callback_data='star_questionnaire')
    markup.add(questionnaire_button)
    return markup
