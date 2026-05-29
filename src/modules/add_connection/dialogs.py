from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Const, Format, Multi
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Next, Cancel, Back, Group
from aiogram_dialog.widgets.input import TextInput
from ipaddress import IPv4Address
from .states import AddHostSG

add_hostname_window_addhostsg = Window(
    Const("Enter IP/Hostname"),
    TextInput(type_factory=IPv4Address, on_success=Next(), id="ip_hostname"),
    Cancel(Const("Back")),
    state=AddHostSG.add_hostname
)

add_port_window_addhostsg = Window(
    Const("Enter port"),
    TextInput(type_factory=int, on_success=Next(), id="port"),
    Back(Const("Back")),
    state=AddHostSG.add_port
)

add_user_window_addhostsg = Window(
    Const("Enter username"),
    TextInput(type_factory=str, on_success=Next(), id="username"),
    Back(Const("Back")),
    state=AddHostSG.add_user
)

add_password_window_addhostsg = Window(
    Const("Enter password"),
    TextInput(type_factory=str, on_success=Next(), id="password"),
    Back(Const("Back")),
    state=AddHostSG.add_password
)

confirm_window_addhostsg = Window(
    Const("Confirm:"),
    Multi(
        Format("IP-address: {ip_hostname}:{port}"),
        Format("Username: {username}"),
        Format("Password: {password}"),
        sep="\n"
    ),
    Group(
        Button(Const("Correct"), id="correct_button"),
        SwitchTo(Const("Rewrite"), state=AddHostSG.add_hostname, id="restart"),
        Cancel(Const("Back to main menu")),
        width=2
    ),
    state=AddHostSG.confirm
)

add_host_sg = Dialog(
    add_hostname_window_addhostsg,
    add_port_window_addhostsg,
    add_user_window_addhostsg,
    add_password_window_addhostsg
)