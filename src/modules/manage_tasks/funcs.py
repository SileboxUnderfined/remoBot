from src.modules.main_menu.states import MainMenuSG
from aiogram_dialog.widgets.kbd import Select, Button
from src.background_manager import task_manager
from aiogram.types import User, CallbackQuery
from aiogram_dialog import DialogManager, StartMode
import logging

async def get_all_tasks(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    user_id: int = event_from_user.id

    tasks: dict[str,str] = task_manager.get_user_tasks(user_id)
    
    return {
        "tasks":list(tasks.items())
    }

async def get_task_info(dialog_manager: DialogManager, **kwargs):
    return {
        "task_id": dialog_manager.dialog_data['task_id']
    }

async def on_task_selected(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    manager.dialog_data['task_id'] = item_id

    await manager.next()

async def kill_task(callback: CallbackQuery, button: Button, manager: DialogManager):
    task_id: str = manager.dialog_data['task_id']
    is_killed: bool = task_manager.cancel_task(task_id)

    if not is_killed:
        await callback.answer("Could not kill task!!")
        return
    
    await callback.answer("Task killed!")
    await manager.start(MainMenuSG.start, mode=StartMode.RESET_STACK)