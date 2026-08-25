import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Ye test pass hoga"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_intentional_failure(client):
    """
    INTENTIONAL FAILURE:
    Expected status 'success' pass kiya hai, jabki app.py 'healthy' return karta hai.
    """
    response = client.get('/')
    assert response.json["status"] == "success"  # <-- Ye assertion fail hoga!