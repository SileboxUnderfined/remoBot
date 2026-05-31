from aiogram.fsm.state import State
from typing import Callable
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Group, Button, SwitchTo, Cancel


def create_confirm_window(
    print_f: Callable,
    save_data_and_quit: Callable,
    rewrite_state: State,
    state: State,
    getter: Callable
) -> Window:
    return Window(
        Const("Confirm:"),
        print_f(),
        Group(
            Button(Const("Correct"), id="correct_button", on_click=save_data_and_quit),
            SwitchTo(Const("Rewrite"), state=rewrite_state, id="restart"),
            Cancel(Const("Back to main menu")),
            width=2
        ),
        state=state,
        getter=getter
    )