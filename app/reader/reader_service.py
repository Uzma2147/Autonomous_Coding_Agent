from app.reader.file_reader import FileReader


class ReaderService:

    @staticmethod
    def read(file_path: str):

        return FileReader.read_file(file_path)