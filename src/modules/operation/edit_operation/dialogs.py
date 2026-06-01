from .funcs import on_operation_selected, get_all_operations, rewrite_operation, delete_operation_btn
from src.modules.elements.prints import print_host, print_operation
from src.modules.elements.select_scroll import select_scroll
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Cancel, Group, Button, Back
from .states import EditOperationSG

select_operation_editoperationsg = select_scroll(
    on_click=on_operation_selected,
    items_key="operations",
    widget_id="operation",
    state=EditOperationSG.select_operation,
    getter=get_all_operations
)

edit_operation_editoperationsg = Window(
    Const("Operation info"),
    print_operation(),
    Group(
        Button(Const("Rewrite"), on_click=rewrite_operation, id="rewrite_btn"),
        Button(Const("Delete"), on_click=delete_operation_btn, id="delete_operation_btn"),
        Back(Const("Back")),
        Cancel(Const("Main Menu")),
        width=2
    ),
    state=EditOperationSG.manage_operation
)

edit_operation_dialog = Dialog(
    select_operation_editoperationsg,
    edit_operation_editoperationsg
)