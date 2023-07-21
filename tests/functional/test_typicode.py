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
