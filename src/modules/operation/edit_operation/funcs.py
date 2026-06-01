from src.modules.operation.add_operation.states import AddOperationSG
from src.models.operation import Operation
from src.modules.main_menu.states import MainMenuSG
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Select, Button
from aiogram.types import CallbackQuery
from typing import List

async def get_all_operations(**kwargs):
    operations: List[Operation] = await Operation.all()
    return {
        "operations":operations
    }

async def on_operation_selected(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    operation: Operation | None = await Operation.get_or_none(label=item_id)
    if operation is None:
        await callback.answer(f"Operation {item_id} not found...")
        return
        
    manager.dialog_data['operation'] = operation

    await manager.next()

async def delete_operation(manager: DialogManager) -> bool:
    operation: Operation | None = manager.dialog_data.get('operation')
    if operation is None:
        return False

    await operation.delete()

    return True

async def rewrite_operation(callback: CallbackQuery, widget: Button, manager: DialogManager):
    if not await delete_operation(manager):
        await callback.answer("Operation not found in dialog_data")
        return

    await manager.start(AddOperationSG.add_command, mode=StartMode.RESET_STACK)

async def delete_operation_btn(callback: CallbackQuery, widget: Button, manager: DialogManager):
    if not await delete_operation(manager):
        await callback.answer("Operation not found in dialog_data")
        return

    await callback.answer("Operation deleted!")
    await manager.start(MainMenuSG.start, mode=StartMode.RESET_STACK)