from src.modules.main_menu.states import MainMenuSG
from aiogram_dialog.widgets.kbd import Group, Button, Start, Back
from aiogram_dialog.widgets.text import Const, Multi, Format
from aiogram_dialog import Dialog, Window, StartMode
from src.modules.manage_tasks.states import ManageTasksSG
from src.modules.manage_tasks.funcs import on_task_selected, get_all_tasks, kill_task, get_task_info
from src.modules.elements.select_scroll import select_scroll

select_task_managetaskssg = select_scroll(
    on_click=on_task_selected,
    getter=get_all_tasks,
    items_key='tasks',
    state=ManageTasksSG.select_task,
    item_id_getter=0,
    label_var='item[1]',
    widget_id='tasks'
)

manage_task_managetaskssg = Window(
    Multi(
        Const("Manage task:"),
        Format("task_id: {task_id}"),
        sep="\n"
    ),
    Group(
        Button(Const("Kill task"), on_click=kill_task, id="kill_task_btn"),
        Back(Const("Back")),
        Start(Const("Main Menu"), state=MainMenuSG.start, mode=StartMode.RESET_STACK, id='main_menu_btn'),
        width=2
    ),
    getter=get_task_info,
    state=ManageTasksSG.manage_task
)

manage_tasks_dialog = Dialog(
    select_task_managetaskssg,
    manage_task_managetaskssg
)