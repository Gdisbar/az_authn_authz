from typing import Annotated
from pydantic import BaseModel


class SingleResponse(BaseModel):
    task_id: str
    user_id: str
    task_name: str
    task_start_time: str
    task_end_time: str
    priority: str
    status: str

