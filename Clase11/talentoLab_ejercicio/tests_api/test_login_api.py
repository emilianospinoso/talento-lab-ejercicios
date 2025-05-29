import pytest
import requests

# Simulamos login validando usuarios existentes
CASOS_LOGIN_API = [
    ("Sincere@april.biz", True, "Usuario válido existente"),
    ("usuario@inexistente.com", False, "Usuario inexistente"),
    ("", False, "Email vacío"),
]

@pytest.mark.api
@pytest.mark.parametrize("email, debe_existir, descripcion", CASOS_LOGIN_API)
def test_validar_usuario_parametrizado(email, debe_existir, descripcion):
    """
    Test parametrizado que simula login validando usuarios existentes
    """
    print(f"\n🔐 Probando: {descripcion}")
    print(f"   Email: {email}")
    
    # Obtener lista de usuarios
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    
    users = response.json()
    
    # Verificar si el usuario existe
    if email:
        user_found = any(user['email'] == email for user in users)
    else:
        user_found = False
    
    if debe_existir:
        assert user_found, f"Usuario {email} debería existir"
        print(f"   ✅ Usuario validado correctamente")
    else:
        assert not user_found, f"Usuario {email} no debería existir"
        print(f"   ❌ Usuario correctamente rechazado")

@pytest.mark.api
@pytest.mark.smoke
def test_validacion_usuario_smoke():
    """
    Test de smoke para verificar que la validación básica funciona
    """
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    
    users = response.json()
    assert len(users) > 0
    
    # Verificar que el primer usuario tiene email
    primer_usuario = users[0]
    assert 'email' in primer_usuario
    assert '@' in primer_usuario['email']
    
    print("✅ Test de smoke de validación de usuario API pasó correctamente")