from aiogram_dialog.widgets.text import Multi, Format

def print_host() -> Multi:
    return Multi(
        Format("Label: {dialog_data[host].label}"),
        Format("IP-address: {dialog_data[host].hostname}:{dialog_data[host].port}"),
        Format("Username: {dialog_data[host].username}"),
        Format("Password: {dialog_data[host].password}"),
        sep="\n"
    )

def print_operation() -> Multi:
    return Multi(
        Format("Label: {dialog_data[operation].label}"),
        Format("Command: {dialog_data[operation].command}"),
        sep="\n"
    )