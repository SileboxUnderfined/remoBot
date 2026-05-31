from aiogram.filters.state import StatesGroup, State

class MainMenuSG(StatesGroup):
    start = State()
    manage_hosts = State()
    manage_operations = State()