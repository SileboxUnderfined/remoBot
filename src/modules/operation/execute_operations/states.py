from aiogram.fsm.state import State, StatesGroup

class ExecuteOperationsSG(StatesGroup):
    select_operations = State()
    select_hosts = State()
    confirm = State()