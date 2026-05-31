import operator
from typing import Callable
from aiogram_dialog.widgets.kbd import ScrollingGroup, Select
from aiogram_dialog.widgets.text import Format

def select_host_scroll(on_click: Callable, items_key: str) -> ScrollingGroup:
    return ScrollingGroup(
        Select(
            Format("{item.label}"),
            id="sel_select_host",
            item_id_getter=operator.attrgetter("label"),
            items=items_key,
            on_click=on_click
        ),
        id="scroll_select_host",
        width=1,
        height=5
    )