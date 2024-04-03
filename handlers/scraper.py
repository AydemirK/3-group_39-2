from aiogram import types, Dispatcher
from config import bot
from scraper.async_scraper import AsyncScraper
from database import sql_queries
from database.async_database import AsyncDatabase


async def news_call(call: types.CallbackQuery):
    db = AsyncDatabase()
    scraper = AsyncScraper()
    links = await scraper.get_pages()
    if links is not None:
        for link in links:
            # await db.execute_query(
            #     query=sql_queries.INSERT_SALE_QUERY,
            #     params=link,
            #     fetch="none"
            #     )
            await bot.send_message(
                chat_id=call.from_user.id,
                text=link
            )
    else:
        print("Ошибка при получении страниц или скрапинге данных.")


def register_news_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        news_call,
        lambda call: call.data == 'news'
    )
