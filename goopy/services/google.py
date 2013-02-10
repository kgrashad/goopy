from service import SearchService, Query, QueryResult
import json
import httplib
import os
import pickle
import urllib

GOOGLE_HOST = "www.googleapis.com"
GOOGLE_URL = "/customsearch/v1?prettyPrint=false&key=%s&cx=%s&%s"
CACHE_FILE = ".cache"

class GoogleService(SearchService):

    def search(self, query):
        url = GOOGLE_URL % (self.config.google_api_key, 
            self.config.google_engine_id, 
            urllib.urlencode({'q': query.keywords}))

        status, response = self._do_get_request(url)
        
        results = []

        if status != 200:
            return QueryResult('Error')
        else:
            data = json.loads(response)
            for item in data['items'][:self.config.max_results]:
                results.append(self._parse_result(item))

        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)

        cache = open(CACHE_FILE, "w")
        pickle.dump(results, cache)
        
        return results

    def get_latest_results(self):
        if not os.path.exists(CACHE_FILE):
            return None

        cache = open(CACHE_FILE, "r")

        return pickle.load(cache)

    def _parse_result(self, json_object):
        return QueryResult(
            json_object['title'],
            json_object['link'],
            json_object['displayLink'],
            json_object['snippet'])

    def _do_get_request(self, url):
        connection = httplib.HTTPSConnection(GOOGLE_HOST)
        connection.request("GET", url)
        response = connection.getresponse()
        return response.status, response.read()

class MockGoogleService(GoogleService):
    """MockService that loads the response from respons.json.
    This service is mainly for testing purposes"""

    def _do_get_request(self, url):
        data = open('services/response.json', 'r').read()
        return 200, data