from pprint import pprint

import requests
from pytest_voluptuous import S
from requests import Response

from schemas.reqres import UnknownListSchema


def test_get_users():
    result: Response = requests.get("https://reqres.in/api/users", params={"page": 2})
    # print(response.status_code)
    pprint(result.request.headers)
    assert result.status_code == 200
    assert result.json()['page'] == 2
    assert len(result.json()['data']) != 0


def test_create_user():
    name = "morpheus_2"
    job = "leader"

    result = requests.post(
        url="https://reqres.in/api/users", json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)


def test_unknown_list_schema(reqres_session):
    result = reqres_session.get('/api/unknown')

    assert result.json() == S(UnknownListSchema)
    assert result.json()['data'][2]['id'] == 3


def test_delete(reqres_session):
    result = reqres_session.delete('/api/users/2')
    assert result.status_code == 204
    assert result.text == ''
