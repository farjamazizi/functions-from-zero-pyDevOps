import pytest
from fastapi.testclient import TestClient

from main import app
from mylib.logistics import find_coordinate, distanse, total_distanse


client = TestClient(app)


def test_find_coordinate():
    assert find_coordinate("Chicago") == (41.8781, -87.6298)


def test_find_coordinate_unknown_city():
    with pytest.raises(ValueError):
        find_coordinate("Boston")


def test_distanse():
    assert distanse("New York", "Chicago") == pytest.approx(711.04, rel=0.01)


def test_total_distanse():
    expected_total = distanse("New York", "Chicago") + distanse("Chicago", "Seattle")
    assert total_distanse(["New York", "Chicago", "Seattle"]) == pytest.approx(
        expected_total
    )


def test_total_distanse_with_one_city():
    assert total_distanse(["Chicago"]) == 0


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello logistics and wiki",
        "endpoints": [
            "/coordinate",
            "/distance",
            "/total-distance",
            "/wiki/search",
            "/wiki/summary",
            "/wiki/url",
        ],
    }


def test_coordinate_endpoint():
    response = client.post("/coordinate", json={"name": "Chicago"})

    assert response.status_code == 200
    assert response.json() == {
        "city": "Chicago",
        "latitude": 41.8781,
        "longitude": -87.6298,
    }


def test_coordinate_endpoint_unknown_city():
    response = client.post("/coordinate", json={"name": "Boston"})

    assert response.status_code == 404
    assert response.json() == {"detail": "City not found: Boston"}


def test_distance_endpoint():
    response = client.post(
        "/distance",
        json={"city1": "New York", "city2": "Chicago"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "from": "New York",
        "to": "Chicago",
        "distance_miles": pytest.approx(711.04, rel=0.01),
    }


def test_total_distance_endpoint():
    response = client.post(
        "/total-distance",
        json={"cities": ["New York", "Chicago", "Seattle"]},
    )

    assert response.status_code == 200
    assert response.json()["cities"] == ["New York", "Chicago", "Seattle"]
    assert response.json()["distance_miles"] == pytest.approx(
        total_distanse(["New York", "Chicago", "Seattle"]),
        rel=0.01,
    )
