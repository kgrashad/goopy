from services.search_service import SearchService, Query, QueryResult
import argparse
import output
import services.service_factory as factory

def main():
    args = _parse_args()

    service = factory.create_search_service(args.engine)

    resultnum = try_get_number(args.query)

    if args.last_query:
        results = service.get_latest_results()
        if results != None:
            output.print_results(results)
    if resultnum != None and 1 <= resultnum <= 10:
        results = service.get_latest_results()
        if results != None and resultnum <= len(results):
            output.print_result(results[resultnum - 1])
        else:
            print "No results found"

    else:
        query = Query(args.query)
        results = service.search(query)
        output.print_results(results)  

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs="?", help='enter the query you want to search')
    parser.add_argument("-e", "--engine", default="google", help="Engine to use")
    parser.add_argument("-l", "--last-query", action="store_false", help="print last query again")
    args = parser.parse_args()
    return args 

def try_get_number(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None

if __name__ == '__main__':
    main()