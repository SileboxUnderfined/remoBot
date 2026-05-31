from aiogram_dialog.widgets.text import Multi, Format

def print_host() -> Multi:
    return Multi(
        Format("Label: {host.label}"),
        Format("IP-address: {host.hostname}:{host.port}"),
        Format("Username: {host.username}"),
        Format("Password: {host.password}"),
        sep="\n"
    )