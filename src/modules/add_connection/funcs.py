from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog import DialogManager

async def getter_confirm_data(dialog_manager: DialogManager, **kwargs):
    return {
        "ip_hostname": dialog_manager.dialog_data['ip_hostname'],
        "port": dialog_manager.dialog_data['port'],
        "username": dialog_manager.dialog_data['username'],
        "password": dialog_manager.dialog_data['password']
    }

async def write_data(): pass # TODO: add