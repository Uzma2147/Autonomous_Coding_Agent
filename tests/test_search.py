from app.search.search_service import SearchService
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


result = SearchService.search_repository(
    repository_path="sample_repo",
    keyword="login"
)

print(result)