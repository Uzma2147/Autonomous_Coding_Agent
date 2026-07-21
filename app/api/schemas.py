from pydantic import BaseModel


class BugRequest(BaseModel):
    title: str
    description: str
    severity: str
    file_path: str
    keyword: str
    repository_path: str