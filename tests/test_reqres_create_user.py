import requests
from pytest_voluptuous import S
from requests import Response

from schemas.reqres import CreateUserSchema


def test_create_user_schema(reqres_session):
    name = "morpheus_2"
    job = "leader"

    result = requests.post(
        url="https://reqres.in/api/users",
        json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(CreateUserSchema)


def test_create_user_schema_v2(reqres_session):
    name = "morpheus_2"
    job = "leader"

    result: Response = reqres_session.post(
        url="/api/users",
        json={"name": name, "job": job}
    )
    print(result.text)
    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(CreateUserSchema)
