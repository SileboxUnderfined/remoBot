from aiogram.filters.state import StatesGroup, State

class AddHostSG(StatesGroup):
    add_hostname = State()
    add_port = State()
    add_user = State()
    add_password = State()
    confirm = State()