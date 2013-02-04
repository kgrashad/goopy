from search_service import SearchService, Query, QueryResult

class MockService(SearchService):

    def search(self, Query):
        result = QueryResult("http://www.google.com/")
        return result
