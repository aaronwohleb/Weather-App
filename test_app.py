import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads successfully."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Secure Weather App" in rv.data

def test_no_api_key_behavior(client, monkeypatch):
    """Test that the app handles missing API keys gracefully (Security Test)."""
    # Temporarily remove API Key from environment to simulate a failure
    monkeypatch.delenv("WEATHER_API_KEY", raising=False)
    
    rv = client.post('/', data={'city': 'London'})
    assert b"API Key is missing" in rv.data