from decouple import config
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config('TOKEN')
MEDIA_DEST = config('MEDIA_DEST')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

