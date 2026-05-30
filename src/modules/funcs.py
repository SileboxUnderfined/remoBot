from typing import Any
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput
from aiogram.types import Message
from aiogram_dialog import DialogManager

async def write_data_and_next(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, data: Any):
    dialog_manager.dialog_data[widget.widget.widget_id] = message.text
    await dialog_manager.next()