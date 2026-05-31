from src.modules.elements.prints import print_host
from .funcs import on_host_selected, get_all_hosts, rewrite_host, delete_host_btn
from src.modules.elements.select_scroll import select_scroll
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Cancel, Group, Button, Back
from .states import EditHostSG

select_host_edithostsg = select_scroll(
    on_click=on_host_selected,
    items_key="hosts",
    widget_id="host",
    state=EditHostSG.select_host,
    getter=get_all_hosts
)

edit_host_edithostsg = Window(
    Const("Host info"),
    print_host(),
    Group(
        Button(Const("Rewrite"), on_click=rewrite_host, id="rewrite_btn"),
        Button(Const("Delete"), on_click=delete_host_btn, id="delete_host_btn"),
        Back(Const("Back")),
        Cancel(Const("Main Menu")),
        width=2
    ),
    state=EditHostSG.manage_host
)

edit_host_dialog = Dialog(
    select_host_edithostsg,
    edit_host_edithostsg
)