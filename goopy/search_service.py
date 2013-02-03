class Query(object):
    def __init__(self, text):
        self.text = text

class QueryResult(object):
    def __init__(self, link):
        self.link = link

class SearchService(object):
    """Abstract class representing a search service"""
    def query(self, Query):
        pass