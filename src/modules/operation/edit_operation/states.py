from aiogram.fsm.state import State, StatesGroup

class EditOperationSG(StatesGroup):
    select_operation = State()
    manage_operation = State()