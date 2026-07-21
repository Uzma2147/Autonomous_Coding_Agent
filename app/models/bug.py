from pydantic import BaseModel
from typing import Optional


class BugReport(BaseModel):
    title: str
    description: str
    severity: str
    file_path: Optional[str] = None