from src.modules.add_connection.states import AddHostSG
from src.modules.main_menu.states import MainMenuSG
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Select, Button
from aiogram.types import CallbackQuery
from typing import List
from src.models.host import Host

async def get_all_hosts(**kwargs):
    hosts: List[Host] = await Host.all()
    return {
        "hosts":hosts
    }

async def on_host_selected(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    host: Host | None = await Host.get_or_none(label=item_id)
    if host is None:
        await callback.answer(f"Host {item_id} not found...")
        return
        
    manager.dialog_data['host'] = host

    await manager.next()

async def delete_host(manager: DialogManager) -> bool:
    host: Host | None = manager.dialog_data.get('host')
    if host is None:
        return False

    await host.delete()

    return True

async def rewrite_host(callback: CallbackQuery, widget: Button, manager: DialogManager):
    if not await delete_host(manager):
        await callback.answer("Host not found in dialog_data")
        return

    await manager.start(AddHostSG.add_hostname, mode=StartMode.RESET_STACK)

async def delete_host_btn(callback: CallbackQuery, widget: Button, manager: DialogManager):
    if not await delete_host(manager):
        await callback.answer("Host not found in dialog_data")
        return

    await callback.answer("Host deleted!")
    await manager.start(MainMenuSG.start, mode=StartMode.RESET_STACK)