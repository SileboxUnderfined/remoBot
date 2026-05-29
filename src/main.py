from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from .settings import settings
from .modules.main_menu.dialogs import main_menu_dialog
from .modules.main_menu.states import MainMenuSG
from aiogram_dialog import setup_dialogs, DialogManager

storage = MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN,)
dp = Dispatcher(storage=storage)
dp.include_router(main_menu_dialog)
setup_dialogs(dp)

@dp.message(CommandStart())
async def start(message: Message, manager: DialogManager):
    await manager.start(MainMenuSG.start)

if __name__ in "__main__":
    dp.run_polling(bot)