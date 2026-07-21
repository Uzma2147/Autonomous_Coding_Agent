import os


class RepositorySearch:

    @staticmethod
    def search_files(repository_path: str, keyword: str):

        matched_files = []

        for root, dirs, files in os.walk(repository_path):

            for file in files:

                if keyword.lower() in file.lower():

                    full_path = os.path.join(root, file)

                    matched_files.append(full_path)

        return matched_files