from app.intake.intake_service import IntakeService
from app.search.search_service import SearchService
from app.diagnosis.diagnosis_service import DiagnosisService

bug = IntakeService.create_bug_report(
    title="Login Crash",
    description="Application crashes when password is empty.",
    severity="High",
    file_path="login.py"
)

search_result = SearchService.search_repository(
    repository_path="sample_repo",
    keyword="login"
)

print(search_result)   

diagnosis = DiagnosisService.diagnose(
    bug,
    search_result
)

print(diagnosis)