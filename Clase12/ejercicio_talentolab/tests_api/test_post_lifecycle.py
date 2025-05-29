import pytest
import requests
import time
from faker import Faker

@pytest.mark.api
@pytest.mark.e2e
def test_post_lifecycle_complete():
    """
    Test end-to-end del ciclo de vida completo de un post:
    1. CREATE (POST)
    2. UPDATE (PATCH) 
    3. DELETE
    """
    fake = Faker('es_ES')
    start_time = time.time()
    
    print("\n🔄 Iniciando ciclo de vida completo de post...")
    
    # PASO 1: CREATE - Crear post con datos aleatorios
    print("📝 PASO 1: Creando post...")
    create_payload = {
        'title': fake.sentence(nb_words=5).rstrip('.'),
        'body': fake.text(max_nb_chars=150),
        'userId': fake.random_int(1, 10)
    }
    
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=create_payload)
    
    # Validaciones CREATE
    assert response.status_code == 201, f"Se esperaba 201, se obtuvo {response.status_code}"
    
    created_post = response.json()
    post_id = created_post['id']
    
    # Validar esquema JSON
    expected_fields = {'id', 'title', 'body', 'userId'}
    assert expected_fields <= set(created_post.keys()), "Faltan campos en la respuesta"
    
    # Validar tipos de datos
    assert isinstance(created_post['id'], int), "ID debe ser entero"
    assert isinstance(created_post['title'], str), "Título debe ser string"
    assert isinstance(created_post['userId'], int), "UserID debe ser entero"
    
    print(f"   ✅ Post creado con ID: {post_id}")
    print(f"   📄 Título: {created_post['title']}")
    
    # PASO 2: UPDATE - Actualizar título usando PATCH
    print("✏️ PASO 2: Actualizando post...")
    update_payload = {'title': 'Título actualizado por QA'}
    
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', 
                             json=update_payload)
    
    # Validaciones UPDATE
    assert response.status_code == 200, f"Se esperaba 200, se obtuvo {response.status_code}"
    
    updated_post = response.json()
    assert updated_post['title'] == 'Título actualizado por QA', "El título no se actualizó correctamente"
    
    # JSONPlaceholder solo devuelve los campos enviados en PATCH
    # Verificamos que al menos el título se actualizó
    assert 'title' in updated_post, "La respuesta debería contener el título"
    
    print(f"   ✅ Post actualizado correctamente")
    print(f"   📝 Nuevo título: {updated_post['title']}")
    
    # PASO 3: DELETE - Eliminar post
    print("🗑️ PASO 3: Eliminando post...")
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    
    # Validaciones DELETE
    assert response.status_code == 200, f"Se esperaba 200, se obtuvo {response.status_code}"
    
    # JSONPlaceholder simula la eliminación
    deleted_response = response.json()
    assert deleted_response == {} or 'id' not in deleted_response, "El post debería estar eliminado"
    
    print(f"   ✅ Post eliminado correctamente")
    
    # VALIDACIÓN FINAL: Performance
    total_time = time.time() - start_time
    assert total_time < 3, f"El flujo tardó {total_time:.2f}s, supera los 3s máximos"
    
    print(f"🎯 CICLO COMPLETADO EXITOSAMENTE en {total_time:.2f}s")

@pytest.mark.api
@pytest.mark.e2e 
def test_post_lifecycle_with_validations():
    """
    Test de ciclo de vida con validaciones avanzadas de headers y performance
    """
    print("\n🔬 Ciclo de vida con validaciones avanzadas...")
    
    # CREATE con validaciones de headers
    payload = {
        'title': 'Test con validaciones avanzadas',
        'body': 'Contenido para testing avanzado',
        'userId': 1
    }
    
    start = time.time()
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    create_time = time.time() - start
    
    # Validaciones CREATE
    assert response.status_code == 201
    
    # Validar headers
    assert 'application/json' in response.headers['Content-Type']
    assert 'charset=utf-8' in response.headers['Content-Type']
    
    # Validar performance
    assert create_time < 1, f"CREATE tardó {create_time:.3f}s, supera 1s"
    
    created_post = response.json()
    post_id = created_post['id']
    
    print(f"   ✅ CREATE validado - Tiempo: {create_time:.3f}s")
    
    # PATCH con validaciones
    start = time.time()
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}',
                             json={'title': 'Título con validaciones'})
    patch_time = time.time() - start
    
    assert response.status_code == 200
    assert patch_time < 1, f"PATCH tardó {patch_time:.3f}s, supera 1s"
    
    # Verificar que el título se actualizó
    updated_data = response.json()
    assert updated_data['title'] == 'Título con validaciones', "El título no se actualizó"
    
    print(f"   ✅ PATCH validado - Tiempo: {patch_time:.3f}s")
    
    # DELETE con validaciones
    start = time.time()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    delete_time = time.time() - start
    
    assert response.status_code == 200
    assert delete_time < 1, f"DELETE tardó {delete_time:.3f}s, supera 1s"
    
    print(f"   ✅ DELETE validado - Tiempo: {delete_time:.3f}s")
    print(f"🎯 Validaciones avanzadas completadas")