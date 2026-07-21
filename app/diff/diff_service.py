from app.diff.diff_generator import DiffGenerator


class DiffService:

    @staticmethod
    def create_diff(
        original: str,
        modified: str
    ) -> str:

        return DiffGenerator.generate(
            original,
            modified
        )