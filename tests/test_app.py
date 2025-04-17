import pytest
from webapp.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Flask" in response.data
    
def test_404(client):
    response = client.get("/non-existent")
    assert response.status_code == 404
