from app.diagnosis.analyzer import BugAnalyzer
from app.models.bug import BugReport
from app.models.search import SearchResult
from app.models.diagnosis import DiagnosisResult


class DiagnosisService:

    @staticmethod
    def diagnose(
        bug: BugReport,
        search: SearchResult
    ) -> DiagnosisResult:

        return BugAnalyzer.analyze(
            bug,
            search
        )