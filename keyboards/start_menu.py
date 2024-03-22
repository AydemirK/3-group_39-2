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
    random_profile_button = InlineKeyboardButton(
        'View Profiles 🎰',
        callback_data='random_profile'
    )
    # markup.add(questionnaire_button)
    # markup.add(group_button)
    markup.add(registration_button)
    markup.add(random_profile_button)
    return markup
