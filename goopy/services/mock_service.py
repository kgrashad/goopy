from google_service import GoogleService

class MockService(GoogleService):
    """MockService that loads the response from respons.json.
    This service is mainly for testing purposes"""

    def __init__(self, config):
        super(config)

    def _do_get_request(self, url):
        data = open('services/response.json', 'r').read()
        return 200, data