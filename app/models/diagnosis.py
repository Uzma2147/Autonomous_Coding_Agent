from pydantic import BaseModel


class DiagnosisResult(BaseModel):
    hypothesis: str
    confidence: float