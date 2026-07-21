from app.patching.patch_generator import PatchGenerator
from app.models.bug import BugReport
from app.models.diagnosis import DiagnosisResult
from app.models.patch import PatchResult


class PatchService:

    @staticmethod
    def generate(
        bug: BugReport,
        diagnosis: DiagnosisResult
    ) -> PatchResult:

        return PatchGenerator.generate_patch(
            bug,
            diagnosis
        )