import pytest
import requests
import time
from faker import Faker
from utils.logger import logger

@pytest.mark.api
@pytest.mark.smoke
def test_post_lifecycle_completo():
    """Test end-to-end del ciclo de vida completo de un post"""
    logger.info("=== INICIANDO CICLO DE VIDA COMPLETO ===")
    
    fake = Faker('es_ES')
    start_time = time.time()
    
    # CREAR POST
    logger.info("PASO 1: Creando post...")
    create_payload = {
        'title': fake.sentence(nb_words=5).rstrip('.'),
        'body': fake.text(max_nb_chars=150),
        'userId': fake.random_int(1, 10)
    }
    
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=create_payload)
    assert response.status_code == 201
    
    created_post = response.json()
    post_id = created_post['id']
    logger.info(f"Post creado con ID: {post_id}")
    
    # ACTUALIZAR POST
    logger.info("PASO 2: Actualizando post...")
    update_payload = {'title': 'Título actualizado por QA'}
    
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', 
                             json=update_payload)
    assert response.status_code == 200
    
    updated_post = response.json()
    assert updated_post['title'] == 'Título actualizado por QA'
    logger.info("Post actualizado correctamente")
    
    # ELIMINAR POST
    logger.info("PASO 3: Eliminando post...")
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200
    logger.info("Post eliminado correctamente")
    
    # VERIFICAR PERFORMANCE
    total_time = time.time() - start_time
    assert total_time < 3
    
    logger.info(f"Ciclo completado en {total_time:.2f}s")
    logger.info("=== CICLO DE VIDA COMPLETADO ===")