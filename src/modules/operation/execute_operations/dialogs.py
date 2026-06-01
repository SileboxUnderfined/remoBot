from src.modules.main_menu.states import MainMenuSG
from aiogram_dialog.widgets.text import Const, List, Multi, Format
from aiogram_dialog import Dialog, Window, StartMode
from src.modules.operation.execute_operations.states import ExecuteOperationsSG
from aiogram_dialog.widgets.kbd import Multiselect, Group, Button, SwitchTo, Back, Start, Column, Row
from src.modules.operation.execute_operations.funcs import get_all_data, continue_button_operations, continue_button_hosts, get_selected_data, on_confirm
from src.modules.elements.select_scroll import select_scroll

select_operations_executeoperationssg = select_scroll(
    on_click=continue_button_operations,
    getter=get_all_data,
    items_key='operations',
    widget_id='operations',
    select_type=Multiselect,
    state=ExecuteOperationsSG.select_operations
)

select_hosts_executeoperationssg = select_scroll(
    on_click=continue_button_hosts,
    getter=get_all_data,
    items_key='hosts',
    widget_id='hosts',
    select_type=Multiselect,
    state=ExecuteOperationsSG.select_hosts
)

confirm_executeoperationssg = Window(
    Multi(
        Const("Confirm:"),
        Const("Selected operations:"),
        List(
            Format("{item[0]}: {item[1]}"),
            items='operations_info'
        ),
        Const("Selected hosts:"),
        List(
            Format("{item[0]}: {item[1]}"),
            items='hosts_info'
        ),
        sep='\n'
    ),
    Group(
        Button(Const("Confirm"),id='confirm_btn', on_click=on_confirm),
        SwitchTo(Const("Rewrite"),id='rewrite_btn',state=ExecuteOperationsSG.select_operations),
        Back(Const("Back")),
        Start(Const("To main menu"), id='to_main_menu_btn',state=MainMenuSG.start, mode=StartMode.RESET_STACK),
        width=2
    ),
    getter=get_selected_data,
    state=ExecuteOperationsSG.confirm
)

execute_operations_dialog = Dialog(
    select_operations_executeoperationssg,
    select_hosts_executeoperationssg,
    confirm_executeoperationssg
)