from src.ssh.ssh_connection import SSHConnection, SSHOperationResult
from aiogram_dialog.widgets.kbd import Button
from aiogram.types import CallbackQuery
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog import DialogManager, StartMode
from src.models.host import Host
from src.modules.main_menu.states import MainMenuSG

async def getter_confirm_data(dialog_manager: DialogManager, **kwargs):
    return {
        "ip_hostname": dialog_manager.dialog_data['ip_hostname'],
        "port": dialog_manager.dialog_data['port'],
        "username": dialog_manager.dialog_data['username'],
        "password": dialog_manager.dialog_data['password'],
        "label": dialog_manager.dialog_data['label']
    }

async def save_data_and_quit(callback: CallbackQuery, button: Button, manager: DialogManager):
    if await Host.filter(label=manager.dialog_data['label']).exists():
        await callback.answer("This host label already exists!")
        return

    host = Host(
        label=manager.dialog_data['label'],
        hostname=manager.dialog_data['ip_hostname'],
        port=manager.dialog_data['port'],
        username=manager.dialog_data['username'],
        password=manager.dialog_data['password'],
    )

    async with SSHConnection(host) as conn:
        conn_result: SSHOperationResult = await conn.check_connection()

    if not conn_result.success:
        await callback.answer(f"Failed while checking connection: {conn_result.result}")

    await host.save()
    await callback.answer("Host successfully added!")
    await manager.start(MainMenuSG.start, mode=StartMode.RESET_STACK)