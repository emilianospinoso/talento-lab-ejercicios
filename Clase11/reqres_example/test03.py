import requests

# Usamos JSONPlaceholder para crear posts (equivalente a crear usuarios)
CREATE_URL = 'https://jsonplaceholder.typicode.com/posts'

def test_create_post():
    payload = {'title': 'Post de Matias QA', 'body': 'Contenido de testing', 'userId': 1}
    
    r = requests.post(CREATE_URL, json=payload)
    assert r.status_code == 201  # Created
    new_post = r.json()
    assert new_post['title'] == 'Post de Matias QA'
    assert 'id' in new_post
    
    print(f"✅ Post creado con ID: {new_post['id']}")
    print(f"📄 Título: {new_post['title']}")

# Para ejecutar como script normal
if __name__ == "__main__":
    test_create_post()
    print("Test completado exitosamente")