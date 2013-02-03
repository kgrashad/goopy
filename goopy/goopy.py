import service_factory
from search_service import SearchService, Query, QueryResult

def main():
    service = service_factory.create_search_service('mock')

    query = Query('test')
    result = service.query(query)
    print result.link

if __name__ == '__main__':
    main()