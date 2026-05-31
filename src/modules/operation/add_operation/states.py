from aiogram.fsm.state import State, StatesGroup

class AddOperationSG(StatesGroup):
    add_command = State()
    add_label = State()
    confirm = State()
    