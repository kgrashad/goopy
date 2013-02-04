import search_service
import google_service
import mock_service


def create_search_service(name):
    if name == 'mock':
        return mock_service.MockService()
    
    if name == 'google':
        return  google_service.GoogleService()