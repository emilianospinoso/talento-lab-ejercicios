import pytest

BASE = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='module')
def posts_url():
    return f"{BASE}/posts"

@pytest.fixture(scope='module') 
def post_by_id_url():
    def _get_url(post_id):
        return f"{BASE}/posts/{post_id}"
    return _get_url


@pytest.mark.api
@pytest.mark.regression
def test_put_post_complete():
    # Test code here
    pass

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

def test_update_created_post(created_post):
    """Usa el post creado en la fixture"""
    post_id = created_post['id']
    
    update_payload = {'title': 'Título actualizado'}
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', 
                             json=update_payload)
    
    assert response.status_code == 200
    assert response.json()['title'] == 'Título actualizado'

