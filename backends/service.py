import json
from pathlib import Path
import asyncio
from typing import List
import aiofiles
from fastapi import APIRouter, Depends, HTTPException
from .model import SingleResponse

router = APIRouter(
    prefix="/api/services",
    responses={404:{"desciption":"Endpoint not found"}}
)

async def get_task_database() -> list[dict]:
    """Dependency that loads and returns the task data json."""
    script_dir = Path(__file__).resolve().parent
    async with aiofiles.open(Path(script_dir / "task_data.json"), "r", encoding="utf-8") as fp:
        contents = await fp.read()
    return [] if not contents else json.loads(contents)

@router.get("/",response_model=list[SingleResponse])
async def get_all_tasks(tasks: list[dict] = Depends(get_task_database)):
    return tasks

@router.get("/{user_id}",response_model=list[SingleResponse])
async def get_one_task(user_id: str,tasks: list[dict] = Depends(get_task_database)):
    user_tasks = [task for task in tasks if task.get("user_id","")==user_id]
    if not user_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this user ID")
    return user_tasks
