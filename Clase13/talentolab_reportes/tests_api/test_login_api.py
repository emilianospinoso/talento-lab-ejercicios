import pytest
import requests
from utils.logger import logger

@pytest.mark.api
@pytest.mark.smoke
def test_validar_usuario_existente():
    """Test que simula login validando usuario existente"""
    logger.info("=== INICIANDO TEST VALIDACIÓN USUARIO API ===")
    
    email_valido = "Sincere@april.biz"
    logger.info(f"Validando usuario con email: {email_valido}")
    
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    
    users = response.json()
    user_found = any(user['email'] == email_valido for user in users)
    assert user_found
    
    logger.info("Usuario validado correctamente")
    logger.info("=== TEST VALIDACIÓN USUARIO COMPLETADO ===")

@pytest.mark.api
def test_validar_usuario_inexistente():
    """Test con usuario que no existe"""
    logger.info("=== INICIANDO TEST USUARIO INEXISTENTE ===")
    
    email_falso = "usuario@inexistente.com"
    logger.info(f"Verificando que no existe: {email_falso}")
    
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    
    users = response.json()
    user_found = any(user['email'] == email_falso for user in users)
    assert not user_found
    
    logger.info("Usuario inexistente verificado correctamente")
    logger.info("=== TEST USUARIO INEXISTENTE COMPLETADO ===")