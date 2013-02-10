import service
import google

def create(name, config):
    if name == 'mock':
        return google.MockGoogleService(config)
    
    if name == 'google':
        return  google.GoogleService(config)