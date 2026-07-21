from pydantic import BaseModel


class PatchResult(BaseModel):

    file_path: str

    patched_code: str

    diff: str