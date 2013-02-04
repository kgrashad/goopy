import service_factory
from search_service import SearchService, Query, QueryResult

def main():
    service = service_factory.create_search_service('google')

    query = Query('test')
    results = service.search(query)

    for result in results:
        print result.title
        print result.snippet
        print

if __name__ == '__main__':
    main()