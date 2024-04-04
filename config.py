from decouple import config
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


PROXY_URL = 'http://proxy.server:3128'
storage = MemoryStorage()
TOKEN = config('TOKEN')
MEDIA_DEST = config('MEDIA_DEST')
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)

