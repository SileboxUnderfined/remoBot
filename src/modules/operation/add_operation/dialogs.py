from src.modules.elements.confirm_window import create_confirm_window
from src.modules.funcs import write_data_and_next
from src.modules.elements.get_text_window import create_get_text_window
from src.modules.elements.prints import print_operation
from .states import AddOperationSG
from .funcs import save_data_and_quit, getter_confirm_data
from aiogram_dialog import Dialog

add_command_window_addoperationsg = create_get_text_window(
    name="Command",
    type_factory=str,
    on_success=write_data_and_next,
    use_cancel=True,
    state=AddOperationSG.add_command
)

add_label_window_addoperationsg = create_get_text_window(
    name="Label",
    type_factory=str,
    on_success=write_data_and_next,
    state=AddOperationSG.add_label
)

confirm_window_addoperationsg = create_confirm_window(
    print_f=print_operation,
    save_data_and_quit=save_data_and_quit,
    rewrite_state=AddOperationSG.add_command,
    state=AddOperationSG.confirm,
    getter=getter_confirm_data
)

add_opeation_dialog = Dialog(
    add_command_window_addoperationsg,
    add_label_window_addoperationsg,
    confirm_window_addoperationsg
)