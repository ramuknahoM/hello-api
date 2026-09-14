from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_hello_world():
    response = client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
