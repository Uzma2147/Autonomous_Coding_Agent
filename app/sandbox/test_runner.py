import subprocess
import re
import time

from app.models.test_result import TestResult


class TestRunner:

    @staticmethod
    def run_tests(repository_path: str) -> TestResult:

        start = time.time()

        try:

            result = subprocess.run(
                ["pytest", "-q"],
                cwd=repository_path,
                capture_output=True,
                text=True
            )

            end = time.time()

            output = result.stdout
            errors = result.stderr

            passed = 0
            failed = 0
            total = 0

            # Parse pytest summary
            passed_match = re.search(r"(\d+) passed", output)
            failed_match = re.search(r"(\d+) failed", output)

            if passed_match:
                passed = int(passed_match.group(1))

            if failed_match:
                failed = int(failed_match.group(1))

            total = passed + failed

            return TestResult(
                success=result.returncode == 0,
                total_tests=total,
                passed_tests=passed,
                failed_tests=failed,
                execution_time=round(end - start, 2),
                output=output,
                errors=errors
            )

        except Exception as e:

            return TestResult(
                success=False,
                total_tests=0,
                passed_tests=0,
                failed_tests=0,
                execution_time=0,
                output="",
                errors=str(e)
            )