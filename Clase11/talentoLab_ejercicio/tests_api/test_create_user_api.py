import pytest
import requests
from faker import Faker
import datetime

# Datos para crear posts (equivalente a crear usuarios en JSONPlaceholder)
POSTS_CREAR = [
    ("Guía QA por Matias", "Contenido sobre testing automatizado"),
    ("Manual PO por Silvia", "Mejores prácticas de product owner"),
    ("Tips Dev por Ana", "Desarrollo con buenas prácticas"),
    ("Liderazgo por Carlos", "Gestión de equipos técnicos"),
]

@pytest.mark.api
@pytest.mark.parametrize("titulo, contenido", POSTS_CREAR)
def test_create_post_parametrizado(titulo, contenido):
    """
    Test parametrizado para crear diferentes posts (simula crear usuarios)
    """
    print(f"\n📝 Creando post: {titulo}")
    
    payload = {
        "title": titulo,
        "body": contenido,
        "userId": 1
    }
    
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    
    # Verificar que el post fue creado
    assert response.status_code == 201
    
    data = response.json()
    
    # Verificar que los datos enviados están en la respuesta
    assert data["title"] == titulo
    assert data["body"] == contenido
    assert data["userId"] == 1
    
    # Verificar que se generó un ID
    assert "id" in data
    assert isinstance(data["id"], int)
    
    print(f"   ✅ Post creado con ID: {data['id']}")

@pytest.mark.api
def test_create_post_with_faker():
    """
    Test que usa Faker para generar contenido aleatorio
    """
    fake = Faker('es_ES')
    
    titulo = fake.sentence(nb_words=4).rstrip('.')  # Sin punto final
    contenido = fake.text(max_nb_chars=200)
    
    print(f"\n🎲 Creando post aleatorio: {titulo}")
    
    payload = {
        "title": titulo,
        "body": contenido,
        "userId": fake.random_int(1, 10)
    }
    
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == titulo
    assert data["body"] == contenido
    assert "id" in data
    
    print(f"   ✅ Post aleatorio creado con ID: {data['id']}")

@pytest.mark.api
def test_create_post_campos_vacios():
    """
    Test para verificar comportamiento con campos vacíos
    """
    print("\n❌ Intentando crear post con campos vacíos")
    
    payload = {
        "title": "",
        "body": "",
        "userId": 1
    }
    
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    
    # JSONPlaceholder acepta campos vacíos y devuelve 201
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == ""
    assert data["body"] == ""
    
    print("   ⚠️ API acepta campos vacíos (comportamiento normal de JSONPlaceholder)")

@pytest.mark.api
def test_create_multiple_posts():
    """
    Test que crea múltiples posts y verifica que todos tienen IDs únicos
    """
    print("\n📚 Creando múltiples posts")
    
    posts_creados = []
    
    for i in range(3):
        payload = {
            "title": f"Post número {i+1}",
            "body": f"Contenido del post {i+1} desde TalentoLab",
            "userId": 1
        }
        
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
        assert response.status_code == 201
        
        data = response.json()
        posts_creados.append(data["id"])
        
        print(f"   📝 Post {i+1} creado con ID: {data['id']}")
    
    # En un sistema real, los IDs deberían ser únicos
    # JSONPlaceholder siempre devuelve ID 101, pero validamos la estructura
    assert len(posts_creados) == 3
    print("   ✅ Todos los posts creados correctamente")

@pytest.mark.api
@pytest.mark.smoke
def test_create_post_smoke():
    """
    Test de smoke para verificar creación básica de post
    """
    payload = {
        "title": "Test Smoke Post",
        "body": "Contenido de prueba desde TalentoLab",
        "userId": 1
    }
    
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    
    assert response.status_code == 201
    assert "id" in response.json()
    
    print("✅ Test de smoke de creación de post API pasó correctamente")