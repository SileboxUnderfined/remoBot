from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Const, Format, Multi
from aiogram_dialog.widgets.kbd import Button, SwitchTo, Next, Cancel, Back, Group
from aiogram_dialog.widgets.input import TextInput
from ipaddress import IPv4Address
from .states import AddHostSG
from src.modules.funcs import write_data_and_next
from .funcs import getter_confirm_data, save_data_and_quit
from src.modules.elements.get_text_window import create_get_text_window

add_hostname_window_addhostsg = create_get_text_window(
    name="IP/Hostname",
    type_factory=IPv4Address,
    on_success=write_data_and_next,
    use_cancel=True,
    state=AddHostSG.add_hostname
)

add_port_window_addhostsg = create_get_text_window(
    name="Port",
    type_factory=int,
    on_success=write_data_and_next,
    state=AddHostSG.add_port
)

add_user_window_addhostsg = create_get_text_window(
    name="Username",
    type_factory=str,
    on_success=write_data_and_next,
    state=AddHostSG.add_user
)

add_password_window_addhostsg = create_get_text_window(
    name="Password",
    type_factory=str,
    on_success=write_data_and_next,
    state=AddHostSG.add_password
)

add_label_window_addhostsg = create_get_text_window(
    name="Label",
    type_factory=str,
    on_success=write_data_and_next,
    state=AddHostSG.add_label
)

confirm_window_addhostsg = Window(
    Const("Confirm:"),
    Multi(
        Format("Label: {label}"),
        Format("IP-address: {ip_hostname}:{port}"),
        Format("Username: {username}"),
        Format("Password: {password}"),
        sep="\n"
    ),
    Group(
        Button(Const("Correct"), id="correct_button", on_click=save_data_and_quit),
        SwitchTo(Const("Rewrite"), state=AddHostSG.add_hostname, id="restart"),
        Cancel(Const("Back to main menu")),
        width=2
    ),
    state=AddHostSG.confirm,
    getter=getter_confirm_data
)

add_host_dialog = Dialog(
    add_hostname_window_addhostsg,
    add_port_window_addhostsg,
    add_user_window_addhostsg,
    add_password_window_addhostsg,
    add_label_window_addhostsg,
    confirm_window_addhostsg
)