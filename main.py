from aiogram import executor, Dispatcher
from config import dp
from database import bot_db
from handlers import (
    start, questionaire, group_action,
    group_questionaire, registration, profile, reference, scraper
)


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_table()


start.register_start_handlers(dp=dp)
questionaire.register_questionnaire_handlers(dp=dp)
group_questionaire.register_group_start_handlers(dp=dp)
registration.register_handler(dp=dp)
group_action.register_group_actions_handler(dp=dp)
profile.register_profile_handlers(dp=dp)
reference.register_reference_handlers(dp=dp)
# scraper.register_news_handlers(dp=dp)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
