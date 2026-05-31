from src.modules.edit_connection.states import EditHostSG
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Const, Multi
from aiogram_dialog.widgets.kbd import Group, Next, Back, Button, SwitchTo, Start, Cancel, Column, Row
from .states import MainMenuSG
from src.modules.add_connection.states import AddHostSG

start_window_mainsg = Window(
    Multi(
        Const("Welcome"),
    ),
    Group(
        SwitchTo(Const("Manage Hosts"),state=MainMenuSG.manage_hosts,id="manage_hosts_st"),
        width=2
    ),
    state=MainMenuSG.start
)

manage_hosts_window_mainsg = Window(
    Const("Manage Hosts"),
    Column(
        Group(
            Start(Const("Add new Host"),id="add_new_host_st",state=AddHostSG.add_hostname),
            Start(Const("Edit Host"),id="edit_host_st", state=EditHostSG.select_host),
            #Start(Const("Singular operations"),id="singular_operations_st"),
            #Start(Const("Multiple operations"),id="multiple_operations_st"),
            width=2
        ),
        Back(Const("Back"))
    ),
    state=MainMenuSG.manage_hosts
)

main_menu_dialog = Dialog(
    start_window_mainsg,
    manage_hosts_window_mainsg
)