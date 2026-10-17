# 📁 Project: az_authn_authz

**📊 Project Overview (Selected Files):**
- Total Files: 7
- Total Size: 2.94 KB
- Total Lines: 106
- Estimated Tokens: ~754 (approx. for LLMs)

**📋 Top File Types:**
- .py: 5
- .json: 1
- .txt: 1

🔖 Legend: ✓=included · ✗=excluded · 📂=folder

## 🌳 Project Structure

```
az_authn_authz/
├── 📂 backends/
│   ├── __init__.py ✓
│   ├── model.py ✓
│   ├── service.py ✓
│   └── task_data.json ✓
├── __init__.py ✓
├── main.py ✓
└── requirements.txt ✓
```

## 📄 Files Content

*Files are listed in alphabetical order by path.*

================================================================================
📄 **__init__.py**
Size: 0 B | Lines: 1
================================================================================

```python

```

================================================================================
📄 **backends\__init__.py**
Size: 0 B | Lines: 1
================================================================================

```python

```

================================================================================
📄 **backends\model.py**
Size: 311 B | Lines: 15
================================================================================

```python
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

class AllResponses(BaseModel):
    all_tasks: list[SingleResponse]
```

================================================================================
📄 **backends\service.py**
Size: 1.11 KB | Lines: 30
================================================================================

```python
import json
from pathlib import Path
import asyncio
import aiofiles
from fastapi import APIRouter, Depends, HTTPException
from .model import SingleResponse,AllResponses

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

@router.get("/",response_model=AllResponses)
async def get_all_tasks(tasks: list[dict] = Depends(get_task_database)):
    return tasks

@router.get("/{user_id}",response_model=SingleResponse)
async def get_one_task(user_id: str,tasks: list[dict] = Depends(get_task_database)):
    user_tasks = [task for task in tasks if task.get("user_id","")==user_id]
    if not user_tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this user ID")
    return user_tasks

```

================================================================================
📄 **backends\task_data.json**
Size: 1.36 KB | Lines: 47
================================================================================

```json
[
  {
    "task_id": "TSK-1001",
    "user_id": "USR-4521",
    "task_name": "Fix authentication token expiration bug",
    "task_start_time": "2026-10-17T08:30:00Z",
    "task_end_time": "2026-10-17T12:00:00Z",
    "priority": "Critical",
    "status": "InProgress"
  },
  {
    "task_id": "TSK-1002",
    "user_id": "USR-4521",
    "task_name": "Update API documentation for v2 endpoints",
    "task_start_time": "2026-10-17T13:00:00Z",
    "task_end_time": "2026-10-17T17:00:00Z",
    "priority": "Medium",
    "status": "Pending"
  },
  {
    "task_id": "TSK-1003",
    "user_id": "USR-8902",
    "task_name": "Database migration backup and verification",
    "task_start_time": "2026-10-16T22:00:00Z",
    "task_end_time": "2026-10-16T23:30:00Z",
    "priority": "High",
    "status": "Completed"
  },
  {
    "task_id": "TSK-1004",
    "user_id": "USR-3314",
    "task_name": "Design system dark mode color palette review",
    "task_start_time": "2026-10-18T09:00:00Z",
    "task_end_time": "2026-10-18T11:00:00Z",
    "priority": "Low",
    "status": "InQueue"
  },
  {
    "task_id": "TSK-1005",
    "user_id": "USR-8902",
    "task_name": "Configure automated security vulnerability scans",
    "task_start_time": "2026-10-18T14:00:00Z",
    "task_end_time": "2026-10-18T16:00:00Z",
    "priority": "High",
    "status": "Pending"
  }
]
```

================================================================================
📄 **main.py**
Size: 142 B | Lines: 9
================================================================================

```python
from fastapi import FastAPI
from backends import service

app = FastAPI()

# app.add_middleware()

app.include_router(service.router)

```

================================================================================
📄 **requirements.txt**
Size: 26 B | Lines: 3
================================================================================

```
fastapi
uvicorn
aiofiles
```

---
*Generated by Codebase Prompt Packer for VS Code*
*Total files processed: 7 | Generated on: 10/17/2026, 12:22:22 PM*
