from fastapi.testclient import TestClient

from main import app

def test_get_products() -> None:
    client = TestClient(app)
    response = client.get("/lists/1/products")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 3

def test_get_product() -> None:
    client = TestClient(app)
    response = client.get("/lists/1/products/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1

    response = client.get("/lists/1/products/412")
    assert response.status_code == 404

def test_update_product() -> None:
    client = TestClient(app)

    data = {
        "id": 1,
        "name": "New item",
        "quantity": 123,
    }
    response = client.put("/lists/1/products/1", json=data)
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "New item"
    assert data["quantity"] == 123

    response = client.put("/lists/1/products/412", json=data)
    assert response.status_code == 404

def test_delete_product() -> None:
    client = TestClient(app)
    response = client.delete("/lists/1/products/1")
    data = response.content
    assert response.status_code == 204
    assert data == b""

    response = client.delete("/lists/1/products/412")
    assert response.status_code == 404

