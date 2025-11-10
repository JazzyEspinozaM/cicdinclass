import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Hello from cicdinclass' in rv.data

def test_api(client):
    rv = client.get('/api')
    assert rv.status_code == 200
    assert rv.get_json() == {'message': 'Hello from cicdinclass'}
