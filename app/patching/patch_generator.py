from app.models.bug import BugReport
from app.models.diagnosis import DiagnosisResult
from app.models.patch import PatchResult

from app.reader.reader_service import ReaderService
from app.diff.diff_service import DiffService


class PatchGenerator:

    @staticmethod
    def generate_patch(
        bug: BugReport,
        diagnosis: DiagnosisResult
    ) -> PatchResult:

        # Read source code
        source_code = ReaderService.read(bug.file_path)

        # File not found
        if source_code is None:
            return PatchResult(
                file_path=bug.file_path,
                patched_code="File not found.",
                diff=""
            )

        print("\n========== SOURCE CODE ==========\n")
        print(source_code)

        # Start with original code
        patched_code = source_code

        # -------------------------
        # Login Bug
        # -------------------------
        if "login" in diagnosis.hypothesis.lower():

            patched_code = source_code.replace(
                'if password == "":',
                'if password is None or password == "":'
            )

        # -------------------------
        # Checkout Bug
        # -------------------------
        elif "checkout" in diagnosis.hypothesis.lower():

            patched_code += """

# TODO:
# Validate checkout data before processing payment.
"""

        # -------------------------
        # Default
        # -------------------------
        else:

            patched_code += """

# TODO:
# Review this file for possible bug fixes.
"""

        print("\n========== PATCHED SOURCE CODE ==========\n")
        print(patched_code)

        # Generate Git Diff
        diff = DiffService.create_diff(
            source_code,
            patched_code
        )

        print("\n========== GIT DIFF ==========\n")
        print(diff)

        # Return Patch Result
        return PatchResult(
            file_path=bug.file_path,
            patched_code=patched_code,
            diff=diff
        )