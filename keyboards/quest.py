from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def quest_keyboard():
    markup = InlineKeyboardMarkup()

    blue_button = InlineKeyboardButton(
        'Синий', callback_data='blue'
    )
    red_button = InlineKeyboardButton(
        'Красный', callback_data='red'
    )
    green_button = InlineKeyboardButton(
        'Зеленый', callback_data='green'
    )
    markup.add(blue_button)
    markup.add(red_button)
    markup.add(green_button)
    return markup
