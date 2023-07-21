from apis.typicodes.views import Typicode


class API:
    def __init__(self, resource, url):
        self.resource = resource
        self.url = url


urls = [
    API(Typicode, '/typicode')
]
