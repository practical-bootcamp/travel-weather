from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == [
        "England", "France", "Germany",
        "Italy", "Peru", "Portugal", "Spain"
    ]


def test_spain_june():
    response = client.get("/countries/Spain/Seville/June")
    assert response.status_code == 200
    assert response.json() == {
        "high": 33.0,
        "low": 19.0,
    }
