import requests

# JSONPlaceholder no tiene login, pero podemos simular con validación de usuario
USERS_URL = 'https://jsonplaceholder.typicode.com/users'

def test_validate_user_exists():
    """Simula un login verificando que un usuario existe"""
    # Obtener todos los usuarios
    response = requests.get(USERS_URL)
    assert response.status_code == 200
    
    users = response.json()
    # Buscar usuario específico (simulando login)
    target_email = "Sincere@april.biz"  # Email real del usuario 1
    
    user_found = any(user['email'] == target_email for user in users)
    assert user_found, f"Usuario con email {target_email} no encontrado"
    
    print(f"✅ Usuario validado correctamente: {target_email}")

def test_validate_user_not_exists():
    """Simula un error de login con usuario inexistente"""
    response = requests.get(USERS_URL)
    assert response.status_code == 200
    
    users = response.json()
    # Buscar usuario que no existe
    fake_email = "usuario@inexistente.com"
    
    user_found = any(user['email'] == fake_email for user in users)
    assert not user_found, f"Usuario {fake_email} no debería existir"
    
    print(f"❌ Usuario inexistente correctamente rechazado: {fake_email}")

# Para ejecutar como script normal
if __name__ == "__main__":
    test_validate_user_exists()
    test_validate_user_not_exists()
    print("Tests completados exitosamente")