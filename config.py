from decouple import config
from aiogram import Dispatcher, Bot

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
