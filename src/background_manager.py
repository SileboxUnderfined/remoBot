import asyncio
import uuid
from typing import Dict, Any

class BackgroundTaskManager:
    def __init__(self):
        self._active_tasks: Dict[str, asyncio.Task]
        self._metadata: Dict[str, Dict[str, Any]] = {}

    def start_task(self, coro, user_id: int, description: str) -> str:
        task_id = str(uuid.uuid4())
        task = asyncio.create_task(coro)

        self._active_tasks[task_id] = task
        self._metadata[task_id] = {
            "user_id":user_id,
            "description":description
        }

        task.add_done_callback(lambda t: self._cleanup(task_id))

        return task_id

    def _cleanup(self, task_id: str):
        self._active_tasks.pop(task_id, None)
        self._metadata.pop(task_id, None)

    def cancel_task(self, task_id: str) -> bool:
        task = self._active_tasks.get(task_id)
        if task and not task.done():
            task.cancel()
            return True

        return False

    def get_user_tasks(self, user_id: int) -> Dict[str, str]:
        return {
            t_id: meta['description']
            for t_id, meta in self._metadata.items()
            if meta['user_id'] == user_id
        }

task_manager = BackgroundTaskManager()