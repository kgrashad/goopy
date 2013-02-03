from search_service import SearchService, Query, QueryResult

class MockService(SearchService):

    def query(self, Query):
        result = QueryResult("http://www.google.com/")
        return result
