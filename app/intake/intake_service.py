
from app.models.bug import BugReport


class IntakeService:

    @staticmethod
    def create_bug_report(
        title: str,
        description: str,
        severity: str,
        file_path: str = None
    ):
           #creates a Pydantic object.
        bug = BugReport(
            title=title,
            description=description,
            severity=severity,
            file_path=file_path
        )

        return bug