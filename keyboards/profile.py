from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def profile_key(telegram_id):
    markup = InlineKeyboardMarkup()

    like_button = InlineKeyboardButton(
        'Like ❤',
        callback_data=f'like_{telegram_id}'
    )
    dislike_button = InlineKeyboardButton(
        'Dislike 🖤',
        callback_data=f'dislike{telegram_id}'
    )

    markup.add(like_button)
    markup.add(dislike_button)
    return markup
