from src.modules.main_menu.states import MainMenuSG
from aiogram_dialog.widgets.kbd import Button
from aiogram.types import CallbackQuery
from src.models.operation import Operation
from aiogram_dialog import DialogManager, StartMode

async def getter_confirm_data(dialog_manager: DialogManager, **kwargs):
   dialog_manager.dialog_data['operation'] = Operation(
       label=dialog_manager.dialog_data['label'],
       command=dialog_manager.dialog_data['command']
   ) 
   return {
       'operation': dialog_manager.dialog_data['operation']
   }

async def save_data_and_quit(callback: CallbackQuery, button: Button, manager: DialogManager):
    operation: Operation = manager.dialog_data['operation']
    if await Operation.exists(label=operation.label):
        await callback.answer("Operation with this label already exists!")
        return

    await operation.save()
    await callback.answer("Operation successfully added!")
    await manager.start(MainMenuSG.start, mode=StartMode.RESET_STACK)