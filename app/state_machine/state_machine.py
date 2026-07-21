from app.state_machine.states import AgentState

from app.intake.intake_service import IntakeService
from app.search.search_service import SearchService
from app.diagnosis.diagnosis_service import DiagnosisService
from app.patching.patch_service import PatchService
from app.sandbox.sandbox_service import SandboxService
from app.reporting.report_service import ReportService


class CodingAgent:

    def __init__(self):

        self.state = AgentState.START

    def run(self):

        print("\n========== AUTONOMOUS CODING AGENT ==========\n")

        # START
        self.state = AgentState.INTAKE
        print("Current State :", self.state)

        title = input("Enter Bug Title: ")

        description = input("Enter Bug Description: ")

        severity = input("Enter Severity (Low/Medium/High): ") 

        file_path = input("Enter File Path: ")

        keyword = input("Enter Search Keyword: ")

        repository = input("Enter Repository Path: ")

        bug = IntakeService.create_bug_report(
        title=title,
        description=description,
        severity=severity,
        file_path=file_path
)

        # SEARCH
        self.state = AgentState.SEARCH
        print("Current State :", self.state)

        search = SearchService.search_repository(
        repository_path=repository,
        keyword=keyword
)

        # DIAGNOSIS
        self.state = AgentState.DIAGNOSIS
        print("Current State :", self.state)

        diagnosis = DiagnosisService.diagnose(
            bug,
            search
        )

        # PATCH
        self.state = AgentState.PATCH
        print("Current State :", self.state)

        patch = PatchService.generate(
            bug,
            diagnosis
        )

        # TEST
        self.state = AgentState.TEST
        print("Current State :", self.state)

        test_result = SandboxService.execute(
        repository
)

        # REPORT
        self.state = AgentState.REPORT
        print("Current State :", self.state)

        report = ReportService.generate_report(
        bug,
        diagnosis,
        patch,
        test_result
)

        print(report)
        # END
        self.state = AgentState.END
        print("\nCurrent State :", self.state)

        print("\nAgent Finished Successfully.")