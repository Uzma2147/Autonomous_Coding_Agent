from fastapi import APIRouter

from app.api.schemas import BugRequest
from app.intake.intake_service import IntakeService
from app.search.search_service import SearchService
from app.diagnosis.diagnosis_service import DiagnosisService
from app.patching.patch_service import PatchService
from app.sandbox.sandbox_service import SandboxService
from app.reporting.report_service import ReportService

router = APIRouter()


@router.post("/analyze")
def analyze_bug(request: BugRequest):

    # Intake
    bug = IntakeService.create_bug_report(
        title=request.title,
        description=request.description,
        severity=request.severity,
        file_path=request.file_path
    )

    # Search
    search = SearchService.search_repository(
        repository_path=request.repository_path,
        keyword=request.keyword
    )

    # Diagnosis
    diagnosis = DiagnosisService.diagnose(
        bug,
        search
    )

    # Patch
    patch = PatchService.generate(
         bug,
         diagnosis
    )

    # Sandbox
    test_result = SandboxService.execute(
        request.repository_path
    )

    # Report
    report = ReportService.generate_report(
        bug,
        diagnosis,
        patch,
        test_result
    )

    return {
        "bug": bug,
        "diagnosis": diagnosis,
        "patch": patch,
        "tests": test_result,
        "report": report
    }