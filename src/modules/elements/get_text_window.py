from aiogram_dialog.widgets.input.text import OnSuccess
from aiogram_dialog.widgets.input import TextInput
from aiogram.fsm.state import State
from aiogram_dialog.widgets.widget_event import WidgetEventProcessor
from typing import Any
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Back, Cancel

def generate_id_from_name(name: str):
    return name.lower().replace("/","_")

def create_get_text_window(name: str, type_factory: Any, on_success: OnSuccess[Any] | WidgetEventProcessor, state: State, use_cancel: bool = False) -> Window:
    return Window(
        Const(f"Enter {name}"),
        TextInput(type_factory=type_factory, on_success=on_success, id=generate_id_from_name(name)),
        Back(Const("Back")) if not use_cancel else Cancel(Const("Back")),
        state=state
    )