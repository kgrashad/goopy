class Query(object):
    def __init__(self, keywords):
        self.keywords = keywords

class QueryResult(object):
    def __init__(self, title, link, snippet):
        self.title = title
        self.link = link
        self.snippet = snippet

class SearchService(object):
    """Abstract class representing a search service"""
    def search(self, Query):
        pass

    def is_available(self):
        pass