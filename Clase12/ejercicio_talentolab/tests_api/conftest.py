import pytest
import requests

BASE = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='module')
def posts_url():
    return f"{BASE}/posts"

@pytest.fixture(scope='module') 
def post_by_id_url():
    def _get_url(post_id):
        return f"{BASE}/posts/{post_id}"
    return _get_url

@pytest.fixture(scope='module')
def created_post():
    """Crea un post y devuelve sus datos para otros tests"""
    payload = {
        'title': 'Post para testing',
        'body': 'Contenido de prueba',
        'userId': 1
    }
    
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    assert response.status_code == 201
    
    return response.json()