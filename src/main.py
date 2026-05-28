from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from .settings import settings

storage = MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN,)