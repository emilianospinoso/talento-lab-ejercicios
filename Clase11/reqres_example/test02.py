import requests
import pytest

# Cambiamos a JSONPlaceholder que funciona sin API key
URL = 'https://jsonplaceholder.typicode.com/users'

def test_get_users():
    r = requests.get(URL)
    assert r.status_code == 200
    data = r.json()
    assert len(data) > 0  # al menos un usuario
    
    # Verificar estructura del primer usuario
    primer_usuario = data[0]
    assert 'id' in primer_usuario
    assert 'email' in primer_usuario
    assert 'name' in primer_usuario
    
    print(f"✅ Se encontraron {len(data)} usuarios")
    print(f"📧 Primer usuario: {primer_usuario['name']} - {primer_usuario['email']}")

# Para ejecutar como script normal
if __name__ == "__main__":
    test_get_users()
    print("Test completado exitosamente")