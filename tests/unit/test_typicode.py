import requests, json

def test_apis_typicodes_service_get_data_typicode():
    headers = {
        'Accept': '*/*',
        'user-Agent': 'request',
        'X-API-KEY': 'Framework'
    }
    url = 'http://localhost:8000/typicode'
    response = requests.get(url, headers=headers)
    assert len(json.loads(response.content)) == 5
    assert response.status_code == 200

def test_apis_typicodes_service_get_data_typicode_error():
    headers = {
        'Accept': '*/*',
        'user-Agent': 'request',
        'X-API-KEY': 'token invalid'
    }
    url = 'http://localhost:8000/typicode'
    response = requests.get(url, headers=headers)
    assert response.status_code == 500

"""import pytest

@pytest.fixture(autouse=True)
def setup(self, test_app):
    self.test_app = test_app


class TestTypicode(object):

    def test_apis_typicodes_service_get_data_typicode(self):
        headers = {
            'Accept': '*/*',
            'user-Agent': 'request',
            'X-API-KEY': 'Framework'
        }
        url = 'http://localhost:8000/typicode'
        response = self.test_app.get(url, headers=headers)
        response_dict = response.json()
        status = response_dict['status']
        response_size = len(response_dict['data'])
        assert status == 'success' and response_size == 5

    def test_apis_typicodes_service_get_data_typicode_error(self):
        headers = {
            'Accept': '*/*',
            'user-Agent': 'request',
            'X-API-KEY': 'token invalid'
        }
        url = 'http://localhost:8000/typicode'
        response = self.test_app.get(url, headers=headers)
        response_dict = response.json()
        assert response.status_code == 403"""