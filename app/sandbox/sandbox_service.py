from app.sandbox.test_runner import TestRunner
from app.models.test_result import TestResult


class SandboxService:

    @staticmethod
    def execute(repository_path: str) -> TestResult:

        return TestRunner.run_tests(repository_path)