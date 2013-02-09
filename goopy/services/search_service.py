class Query(object):
    """Represents a query."""
    def __init__(self, keywords):
        self.keywords = keywords


class QueryResult(object):
    """Represents a query result."""
    def __init__(self, title, link, display_link, snippet):
        self.title = title
        self.link = link
        self.display_link = display_link
        self.snippet = snippet


class SearchService(object):

    def __init__(self, config):
        self.config = config
        
    """Abstract class representing a search service."""
    def search(self, Query):
        """Performs a search on the specified query and return list of results."""
        raise NotImplementedError()

    def get_latest_results(self):
        """Gets the results for the latest queries performed by the service.
        If not results found, None will be returned."""
        raise NotImplementedError()

    def is_available(self):
        """Checks if the service is available."""
        raise NotImplementedError()