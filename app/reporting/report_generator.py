from app.models.bug import BugReport
from app.models.diagnosis import DiagnosisResult
from app.models.patch import PatchResult
from app.models.test_result import TestResult


class ReportGenerator:

    @staticmethod
    def generate(
        bug: BugReport,
        diagnosis: DiagnosisResult,
        patch: PatchResult,
        test: TestResult
    ) -> str:

        report = f"""
=========================================
     AUTONOMOUS CODING AGENT REPORT
=========================================
Test Status:
{"PASSED" if test.success else "FAILED"}

Total Tests:
{test.total_tests}

Passed:
{test.passed_tests}

Failed:
{test.failed_tests}

Execution Time:
{test.execution_time} seconds

Output:
{test.output}

Errors:
{test.errors}
"""

        return report