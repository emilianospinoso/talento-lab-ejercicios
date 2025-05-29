from behave import when, then
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

@when('creo un post con title "{title}" y body "{body}"')
def step_create_post(context, title, body):
    """Crea un nuevo post vía API"""
    payload = {
        'title': title,
        'body': body,
        'userId': 1
    }
    context.response = requests.post(f'{BASE_URL}/posts', json=payload)
    if context.response.status_code == 201:
        context.post_id = context.response.json()['id']

@when('elimino el post recién creado')
def step_delete_post(context):
    """Elimina el post creado anteriormente"""
    if hasattr(context, 'post_id'):
        context.response = requests.delete(f'{BASE_URL}/posts/{context.post_id}')

@when('obtengo la lista de posts')
def step_get_posts(context):
    """Obtiene la lista de todos los posts"""
    context.response = requests.get(f'{BASE_URL}/posts')

@then('la respuesta {method} es {status:d}')
def step_check_status(context, method, status):
    """Verifica el código de estado de la respuesta"""
    assert context.response.status_code == status, (
        f"Esperaba {status}, obtuve {context.response.status_code}")

@then('la respuesta contiene id')
def step_check_id(context):
    """Verifica que la respuesta contenga un ID"""
    data = context.response.json()
    assert 'id' in data, "La respuesta no contiene ID"

@then('la respuesta contiene al menos {count:d} post')
def step_check_posts_count(context, count):
    """Verifica que la respuesta contenga al menos N posts"""
    data = context.response.json()
    assert len(data) >= count, f"Se esperaban al menos {count} posts, se obtuvieron {len(data)}"