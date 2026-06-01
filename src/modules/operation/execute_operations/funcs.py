from src.background_manager import task_manager
from src.modules.main_menu.states import MainMenuSG
import asyncio
from src.ssh.ssh_connection import SSHConnection
from aiogram import Bot
import logging
from aiogram_dialog.widgets.kbd import Multiselect, Button, ManagedMultiselect
from aiogram_dialog import DialogManager, StartMode
from aiogram.types import CallbackQuery
from src.models import Host, Operation

async def get_all_data(**kwargs):
    return {
        'hosts': await Host.all(),
        'operations': await Operation.all()
    }

async def get_selected_data(dialog_manager: DialogManager, **kwargs):
    prepared_operations = ((index+1, item.label) for index, item in enumerate(dialog_manager.dialog_data['selected_operations']))
    prepared_hosts = ((index+1, item.label) for index, item in enumerate(dialog_manager.dialog_data['selected_hosts']))
    return {
        "operations_info":prepared_operations,
        "hosts_info":prepared_hosts
    }

async def continue_button_operations(callback: CallbackQuery, button: Button, manager: DialogManager):
    widget: ManagedMultiselect | None = manager.find("sel_check_operations")
    if widget is None:
        await callback.answer("Could not find Multiselect widget...")
        return

    selected_labels: list[str] = widget.get_checked()
    if len(selected_labels) == 0:
        await callback.answer("You need to select at least 1 opeartion!")
        return

    all_operations: list[Operation] = await Operation.all()

    selected_opeartions: list[Operation] = []
    for operation in all_operations:
        if operation.label in selected_labels:
            selected_opeartions.append(operation)

    manager.dialog_data['selected_operations'] = selected_opeartions
    logging.info(f"selected operations: {selected_opeartions}")
    await manager.next()

async def continue_button_hosts(callback: CallbackQuery, button: Button, manager: DialogManager):
    widget: ManagedMultiselect | None = manager.find("sel_check_hosts")
    if widget is None:
        await callback.answer("Could not find Multiselect widget...")
        return

    selected_labels: list[str] = widget.get_checked()
    if len(selected_labels) == 0:
        await callback.answer("You need to select at least 1 host!")
        return

    all_hosts: list[Host] = await Host.all()

    selected_hosts: list[Host] = []
    for host in all_hosts:
        if host.label in selected_labels:
            selected_hosts.append(host)

    manager.dialog_data['selected_hosts'] = selected_hosts
    logging.info(f"selected hosts: {selected_hosts}")
    await manager.next()

async def on_confirm(callback: CallbackQuery, button: Button, manager: DialogManager):
    hosts = manager.dialog_data['selected_hosts']
    operations = manager.dialog_data['selected_operations']

    if not hosts or not operations:
        await callback.answer("No hosts or operations!")
        return

    if callback.bot is None:
        await callback.answer("No bot!")
        return

    coro = run_operations_background(
        bot=callback.bot,
        chat_id=callback.from_user.id,
        hosts=hosts,
        operations=operations
    )

    description = f"Executing {len(operations)} operations on {len(hosts)} hosts"
    task_manager.start_task(coro, callback.from_user.id, description)
    
    await callback.answer("Operations started!")

    await manager.start(MainMenuSG.start, mode=StartMode.RESET_STACK)

async def run_operations_background(bot: Bot, chat_id: int, hosts: list[Host], operations: list[Operation]):
    await bot.send_message(chat_id, "Started operations in background!")

    for host in hosts:
        try:
            async with SSHConnection(host) as conn:
                for operation in operations:
                    result = await conn.execute_command(operation.command)
                    text = f"✅ <b>{host.label}</b> | <code>{operation.label}</code>\n<pre>{result}</pre>"
                    await bot.send_message(chat_id, text, parse_mode='HTML')
        except Exception as e:
            text =  f"❌ Error at <b>{host.label}</b>:\n<pre>{str(e)}</pre>"
            await bot.send_message(chat_id, text, parse_mode='HTML')

    await bot.send_message(chat_id, "All operations executed on all hosts!")