from pydantic import BaseModel


class TestResult(BaseModel):
    success: bool
    total_tests: int
    passed_tests: int
    failed_tests: int
    execution_time: float
    output: str
    errors: str
  