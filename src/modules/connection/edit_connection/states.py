from aiogram.fsm.state import State, StatesGroup

class EditHostSG(StatesGroup):
    select_host = State()
    manage_host = State()