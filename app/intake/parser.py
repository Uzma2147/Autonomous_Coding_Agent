from app.models.bug import BugReport


class BugParser:

    @staticmethod
    def parse_text(text: str):

        return BugReport(
            title="Unknown Bug",
            description=text,
            severity="Medium"
        )