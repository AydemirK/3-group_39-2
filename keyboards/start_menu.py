from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def start_menu_key():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        'Questionnaire 🎉',
        callback_data='star_questionnaire'
    )
    group_button = InlineKeyboardButton(
        'Ban table check',
        callback_data='ban_check'
    )
    registration_button = InlineKeyboardButton(
        'Registration 📑',
        callback_data='registration'
    )
    my_profile_button = InlineKeyboardButton(
        'Profile',
        callback_data='my_profile'
    )
    random_profile_button = InlineKeyboardButton(
        'View Profiles 🎰',
        callback_data='random_profile'
    )
    reference_menu_button = InlineKeyboardButton(
        'Reference Menu',
        callback_data='reference_menu'
    )
    news_button = InlineKeyboardButton(
        'View News',
        callback_data='news'
    )
    # markup.add(questionnaire_button)
    # markup.add(group_button)
    markup.add(registration_button)
    markup.add(random_profile_button)
    markup.add(my_profile_button)
    markup.add(reference_menu_button)
    markup.add(news_button)
    return markup
