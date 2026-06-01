from src.modules.main_menu.states import MainMenuSG
from aiogram.fsm.state import State
from aiogram_dialog import Window, StartMode
import operator
from typing import Callable, Union
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Start, Button, Multiselect
from aiogram_dialog.widgets.text import Format, Const

def select_scroll(on_click: Callable, items_key: str, widget_id: str, state: State, getter: Callable, select_type: Union[type[Select],type[Multiselect]] = Select) -> Window:
    if select_type is Select:
        list_widget = Select(
            Format("{item.label}"),
            id=f"sel_select_{widget_id}",
            item_id_getter=operator.attrgetter("label"),
            items=items_key,
            on_click=on_click
        )
    elif select_type is Multiselect:
        list_widget = Multiselect(
            Format("✓ {item.label}"),
            Format("{item.label}"),
            id=f"sel_check_{widget_id}",
            item_id_getter=operator.attrgetter('label'),
            items=items_key,
            #on_state_changed=on_click
        )

    widgets: list = [
        ScrollingGroup(
            list_widget,
            id=f"scroll_select_{widget_id}",
            width=1,
            height=5
        )
    ]

    if select_type is Multiselect: 
        widgets.append(Button(Const("Continue"), id=f'next_button_{widget_id}', on_click=on_click))

    return Window(
        Const(f"Select {widget_id}"),
        *widgets,
        Start(Const("Back"), state=MainMenuSG.start, id='back_to_main_menu', mode=StartMode.RESET_STACK),
        state=state,
        getter=getter
    )