from app.models.bug import BugReport
from app.models.search import SearchResult
from app.models.diagnosis import DiagnosisResult


class BugAnalyzer:

    @staticmethod
    def analyze(
        bug: BugReport,
        search: SearchResult
    ) -> DiagnosisResult:



        if len(search.matched_files) == 0:
            return DiagnosisResult(
                hypothesis="No related files were found in the repository.",
                confidence=0.20
            )

        if "login" in bug.title.lower():
            return DiagnosisResult(
                hypothesis="The login module may not be validating user input correctly.",
                confidence=0.85
            )

        if "checkout" in bug.title.lower():
            return DiagnosisResult(
                hypothesis="The checkout process may contain a logic or validation error.",
                confidence=0.80
            )

        return DiagnosisResult(
            hypothesis="Possible bug found in one of the matched files.",
            confidence=0.60
        )