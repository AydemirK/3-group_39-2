from aiogram import types, Dispatcher
from config import bot
from scraper.news_scraper import NewsScraper
from database.bot_db import Database


async def news_call(call: types.CallbackQuery):
    db = Database()
    scraper = NewsScraper()
    links = scraper.scrape()
    for link in links:
        db.sql_insert_sale(link)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=link
        )


def register_news_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        news_call,
        lambda call: call.data == 'news'
    )
