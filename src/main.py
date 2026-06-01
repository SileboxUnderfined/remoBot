from src.modules.manage_tasks.dialogs import manage_tasks_dialog
from src.modules.operation.execute_operations.dialogs import execute_operations_dialog
from src.modules.operation.edit_operation.dialogs import edit_operation_dialog
from .modules.connection.edit_connection.dialogs import edit_host_dialog
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, User
from aiogram.fsm.storage.memory import MemoryStorage
from .settings import settings
from .modules.main_menu.dialogs import main_menu_dialog
from .modules.connection.add_connection.dialogs import add_host_dialog
from .modules.operation.add_operation.dialogs import add_opeation_dialog
from .modules.main_menu.states import MainMenuSG
from aiogram_dialog import setup_dialogs, DialogManager
from tortoise import Tortoise
import asyncio, logging

storage = MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN,)
dp = Dispatcher(storage=storage)
dp.include_router(main_menu_dialog)
dp.include_router(add_host_dialog)
dp.include_router(edit_host_dialog)
dp.include_router(add_opeation_dialog)
dp.include_router(edit_operation_dialog)
dp.include_router(execute_operations_dialog)
dp.include_router(manage_tasks_dialog)
setup_dialogs(dp)

@dp.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    if message.from_user is None: return
    
    if message.from_user.id == settings.ALLOWED_IDS:
        await dialog_manager.start(MainMenuSG.start)

async def main():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models':['src.models']}
    )
    await Tortoise.generate_schemas(safe=True)
    await dp.start_polling(bot)

if __name__ in "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())