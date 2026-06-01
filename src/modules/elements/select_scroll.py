from src.modules.main_menu.states import MainMenuSG
from aiogram.fsm.state import State
from aiogram_dialog import Window, StartMode
import operator
from typing import Callable
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Cancel, Start
from aiogram_dialog.widgets.text import Format, Const

def select_scroll(on_click: Callable, items_key: str, widget_id: str, state: State, getter: Callable) -> Window:
    return Window(
        Const(f"Select {widget_id}"),
        ScrollingGroup(
            Select(
                Format("{item.label}"),
                id=f"sel_select_{widget_id}",
                item_id_getter=operator.attrgetter("label"),
                items=items_key,
                on_click=on_click
            ),
            id=f"scroll_select_{widget_id}",
            width=1,
            height=5
        ),
        Start(Const("Back"), state=MainMenuSG.start, id='back_to_main_menu', mode=StartMode.RESET_STACK),
        state=state,
        getter=getter
    )