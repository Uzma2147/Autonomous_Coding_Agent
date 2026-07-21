import difflib


class DiffGenerator:

    @staticmethod
    def generate(
        original: str,
        modified: str
    ) -> str:

        diff = difflib.unified_diff(
            original.splitlines(),
            modified.splitlines(),
            fromfile="Original",
            tofile="Patched",
            lineterm=""
        )

        return "\n".join(diff)