import requests


def test_a():

    response = requests.get('https://jsonplaceholder.typicode.com/users/1/albums')

    assert response.status_code == 200

