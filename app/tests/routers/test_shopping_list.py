from fastapi.testclient import TestClient

from main import app

def test_get_shopping_lists() -> None:
    client = TestClient(app)
    response = client.get("/lists/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 2

def test_get_shopping_list() -> None:
    client = TestClient(app)
    response = client.get("/lists/2/")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 2
    assert len(data["products"]) == 1

    response = client.get("/lists/1/products/412")
    assert response.status_code == 404
