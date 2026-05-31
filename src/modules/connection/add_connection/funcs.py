from src.ssh.ssh_connection import SSHConnection, SSHOperationResult
from aiogram_dialog.widgets.kbd import Button
from aiogram.types import CallbackQuery
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog import DialogManager, StartMode
from src.models.host import Host
from src.modules.main_menu.states import MainMenuSG

async def getter_confirm_data(dialog_manager: DialogManager, **kwargs):
    dialog_manager.dialog_data['host'] = Host(
        label=dialog_manager.dialog_data['label'],
        hostname=dialog_manager.dialog_data['ip_hostname'],
        port=dialog_manager.dialog_data['port'],
        username=dialog_manager.dialog_data['username'],
        password=dialog_manager.dialog_data['password']
    )
    return {
        "host":dialog_manager.dialog_data['host']
    }

async def save_data_and_quit(callback: CallbackQuery, button: Button, manager: DialogManager):
    host: Host = manager.dialog_data['host']
    if await Host.exists(label=host.label):
        await callback.answer("This host label already exists!")
        return

    try:
        async with SSHConnection(host) as conn:
            conn_result: SSHOperationResult = await SSHConnection.check_connection(conn)

    except Exception as e:
        await callback.answer(f"Failed while connecting to server: {e}")

    if not conn_result.success:
        await callback.answer(f"Failed while checking connection: {conn_result.result}")
        return

    await host.save()
    await callback.answer("Host successfully added!")
    await manager.start(MainMenuSG.start, mode=StartMode.RESET_STACK)