from app.search.repository_search import RepositorySearch
from app.models.search import SearchResult


class SearchService:

    @staticmethod
    def search_repository(repository_path: str, keyword: str):

        results = RepositorySearch.search_files(
            repository_path,
            keyword
        )

        return SearchResult(
            query=keyword,
            matched_files=results
        )