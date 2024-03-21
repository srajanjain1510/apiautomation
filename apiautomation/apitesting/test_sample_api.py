import requests


def test_a():

    response = requests.get('https://jsonplaceholder.typicode.com/users/1/albums')

    response_json = response.json()
    user_id = response_json["userId"]
    user_id_set = set(user_id)

    assert user_id_set == 1

    assert response.status_code == 200

