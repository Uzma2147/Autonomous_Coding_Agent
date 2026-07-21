from pydantic import BaseModel
from typing import List


class SearchResult(BaseModel):
    query: str
    matched_files: List[str]