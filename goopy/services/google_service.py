from search_service import SearchService, Query, QueryResult
import json
import httplib
import urllib

# !!! FIX: this should be configurable
API_KEY = "AIzaSyDxTFivVL_Ly5QTRPK8FeNk9sxN8S35tT0"
SEARCH_ENGINE_ID = "017576662512468239146:omuauf_lfve"

GOOGLE_HOST = "www.googleapis.com"
GOOGLE_URL = "/customsearch/v1?key=%s&cx=%s&%s"

class GoogleService(SearchService):

    def search(self, query):
        url = GOOGLE_URL % (API_KEY, SEARCH_ENGINE_ID, urllib.urlencode({'q': query.keywords}))
        status, response = self._mock_get_request(url)
        results = []

        if status != 200:
            return QueryResult('Error')
        else:
            data = json.loads(response)
            for item in data['items']:
                results.append(self._parse_result(item))
        
        return results

    def _parse_result(self, json_object):
        return QueryResult(json_object['title'], json_object['link'], json_object['snippet'])

    def _do_get_request(self, url):
        connection = httplib.HTTPSConnection(GOOGLE_HOST)
        connection.request("GET", url)
        response = connection.getresponse()
        return response.status, response.read()

    def _mock_get_request(self, url):
        data = open('services/response.json', 'r').read()
        return 200, data
