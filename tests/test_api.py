from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_find_nearby_properties():
    # Test with known location
    response = client.post(
        "/find-nearby-properties",
        json={"query": "Jaipur"}
    )
    assert response.status_code == 200
    assert len(response.json()["results"]) >= 1
    
    # Test with misspelled location
    response = client.post(
        "/find-nearby-properties",
        json={"query": "delih"}
    )
    assert response.status_code == 200
    
    # Test with no nearby properties
    response = client.post(
        "/find-nearby-properties",
        json={"query": "Chennai"}
    )
    assert response.status_code == 200
    assert len(response.json()["results"]) == 0