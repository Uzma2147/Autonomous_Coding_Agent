from app.reporting.report_generator import ReportGenerator


class ReportService:

    @staticmethod
    def generate_report(
        bug,
        diagnosis,
        patch,
        test
    ):

        return ReportGenerator.generate(
            bug,
            diagnosis,
            patch,
            test
        )