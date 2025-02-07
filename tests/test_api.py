from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

def test_classify_number():
    response = client.get("/api/classify-number", params={"number": "28"})
    assert response.status_code == 200
    data = response.json()
    assert data["number"] == 28
    assert data["is_prime"] == False
    assert data["is_perfect"] == True
    assert "even" in data["properties"]
