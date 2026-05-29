from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from .settings import settings
from .modules.main_menu.dialogs import main_menu_dialog
from .modules.main_menu.states import MainMenuSG
from aiogram_dialog import setup_dialogs, DialogManager
from tortoise import Tortoise, run_async

storage = MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN,)
dp = Dispatcher(storage=storage)
dp.include_router(main_menu_dialog)
setup_dialogs(dp)

@dp.message(CommandStart())
async def start(message: Message, manager: DialogManager):
    await manager.start(MainMenuSG.start)

async def main():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models':['models']}
    )
    await dp.start_polling(bot)

if __name__ in "__main__":
    run_async(main())