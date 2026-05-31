from src.modules.connection.edit_connection.states import EditHostSG
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Const, Multi
from aiogram_dialog.widgets.kbd import Group, Next, Back, Button, SwitchTo, Start, Cancel, Column, Row
from .states import MainMenuSG
from src.modules.connection.add_connection.states import AddHostSG

start_window_mainsg = Window(
    Multi(
        Const("Welcome"),
    ),
    Group(
        SwitchTo(Const("Manage Hosts"),state=MainMenuSG.manage_hosts,id="manage_hosts_st"),
        SwitchTo(Const("Manage Operations"),state=MainMenuSG.manage_operations,id="manage_operations_st"),
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
            width=2
        ),
        Back(Const("Back"))
    ),
    state=MainMenuSG.manage_hosts
)

manage_operations_window_mainsg = Window(
    Const("Manage Operations"),
    Column(
        Group(
            Start(Const("Add new Operation"),id="add_new_opeartion_st",state=AddHostSG.add_hostname),
            Start(Const("Edit Operation"),id="edit_host_st", state=EditHostSG.select_host),
            #Start(Const("Execute Operation(s)"))
            width=2
        ),
        Back(Const("Back"))
    ),
    state=MainMenuSG.manage_operations
)

main_menu_dialog = Dialog(
    start_window_mainsg,
    manage_hosts_window_mainsg
)