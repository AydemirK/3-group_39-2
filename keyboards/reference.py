from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def reference_menu_key():
    markup = InlineKeyboardMarkup()

    reference_link_button = InlineKeyboardButton(
        'Link 💥',
        callback_data='reference_link'
    )
    users_list_link_button = InlineKeyboardButton(
        'List of users who clicked on the link',
        callback_data='List_of_users'
    )

    markup.add(reference_link_button)
    markup.add(users_list_link_button)
    return markup
