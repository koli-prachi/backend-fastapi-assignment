from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_register():
    response = client.post("/api/v1/register", json={
        "name": "Prachi",
        "email": "prachi@test.com",
        "password": "123456"
    })
    assert response.status_code == 200