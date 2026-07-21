from pathlib import Path


class FileReader:

    @staticmethod
    def read_file(file_path: str):

        path = Path(file_path)

        if not path.exists():
            return None

        with open(path, "r", encoding="utf-8") as file:
            return file.read()