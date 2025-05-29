import pytest
import requests

@pytest.mark.api
def test_get_users_page_all():
    """
    Test que obtiene todos los usuarios y verifica la estructura
    """
    print("\n👥 Obteniendo todos los usuarios")
    
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    # Verificar status code
    assert response.status_code == 200
    
    # Verificar que tenemos usuarios
    usuarios = response.json()
    assert len(usuarios) > 0, "Debería haber al menos un usuario"
    
    print(f"   👤 Usuarios encontrados: {len(usuarios)}")
    
    # Verificar estructura de cada usuario
    for i, usuario in enumerate(usuarios[:3]):  # Solo los primeros 3 para no saturar
        campos_requeridos = {"id", "email", "name", "username"}
        campos_usuario = set(usuario.keys())
        
        assert campos_requeridos <= campos_usuario, \
            f"Usuario {i+1} no tiene todos los campos requeridos"
        
        # Verificar formato de email
        assert "@" in usuario["email"], f"Email inválido para usuario {usuario['id']}"
        
        print(f"   ✅ Usuario {i+1}: {usuario['name']} - {usuario['email']}")

@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_users_by_id(user_id):
    """
    Test parametrizado para verificar usuarios específicos
    """
    print(f"\n👤 Obteniendo usuario con ID {user_id}")
    
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    assert response.status_code == 200
    
    usuario = response.json()
    assert usuario["id"] == user_id
    assert "email" in usuario
    assert "name" in usuario
    
    print(f"   ✅ Usuario {user_id}: {usuario['name']}")

@pytest.mark.api
def test_get_single_user():
    """
    Test para obtener un usuario específico
    """
    user_id = 2
    print(f"\n👤 Obteniendo usuario con ID {user_id}")
    
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    assert response.status_code == 200
    
    usuario = response.json()
    assert usuario["id"] == user_id
    assert "email" in usuario
    assert "name" in usuario
    assert "address" in usuario  # JSONPlaceholder incluye dirección
    
    print(f"   ✅ Usuario encontrado: {usuario['name']}")
    print(f"   🏠 Ciudad: {usuario['address']['city']}")

@pytest.mark.api
def test_get_user_not_found():
    """
    Test para verificar manejo de usuario inexistente
    """
    user_id = 999
    print(f"\n🔍 Buscando usuario inexistente con ID {user_id}")
    
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    
    assert response.status_code == 404
    print("   ✅ Error 404 retornado correctamente para usuario inexistente")