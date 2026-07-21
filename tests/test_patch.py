from app.intake.intake_service import IntakeService
from app.search.search_service import SearchService
from app.diagnosis.diagnosis_service import DiagnosisService
from app.patching.patch_service import PatchService

bug = IntakeService.create_bug_report(
    title="Login Crash",
    description="Application crashes when password is empty.",
    severity="High",
    file_path="sample_repo/login.py"
)

search = SearchService.search_repository(
    repository_path="sample_repo",
    keyword="login"
)

diagnosis = DiagnosisService.diagnose(
    bug,
    search
)

patch = PatchService.generate(
    bug,
    diagnosis
)

print("\n========== PATCH RESULT ==========")
print("File:", patch.file_path)

print("\nOriginal Code:")
print(patch.original_code)

print("\nPatched Code:")
print(patch.patched_code)