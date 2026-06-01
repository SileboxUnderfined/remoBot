from aiogram.fsm.state import State, StatesGroup

class ManageTasksSG(StatesGroup):
    select_task = State()
    manage_task = State()