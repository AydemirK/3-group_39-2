from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_key():
    markup = InlineKeyboardMarkup()

    questionnaire_button = InlineKeyboardButton('Какой ваш любимый цвет?', callback_data='star_questionnaire')

    markup.add(questionnaire_button)

    return markup


async def start_group_key():
    group_markup = InlineKeyboardMarkup()

    group_button = InlineKeyboardButton('проверка таблиц банов', callback_data='ban_check')

    group_markup.add(group_button)

    return group_markup
