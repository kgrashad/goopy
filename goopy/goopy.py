from services.service import SearchService, Query, QueryResult
import argparse
import json
import output
import os
import services.factory

def main():
    args = _parse_args()

    service = services.factory.create(args.engine, Config())

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
    parser.add_argument("-l", "--last-query", action="store_true", help="print last query again")
    args = parser.parse_args()
    return args 

def try_get_number(s):
    try:
        return int(s)
    except (TypeError, ValueError):
        return None


class Config(object):
    def __init__(self):
        if os.path.exists("config-dev.json"):
            self.load_and_validate("config-dev.json")
        elif os.path.exists("config.json"):
            self.load_and_validate("config.json")
        else:
            raise IOError("Config.json file is missing")

    def load_and_validate(self, filename):
        self.__dict__ = json.load(open(filename, "r"))

        if self.google_api_key == None:
            raise ValueError("google_api_key is missing")

        if self.google_engine_id == None:
            raise ValueError("google_engine_id is missing")

if __name__ == '__main__':
    main()