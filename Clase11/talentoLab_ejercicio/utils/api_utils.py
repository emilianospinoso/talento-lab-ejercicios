import requests
import json
from typing import Dict, Any

class APIClient:
    """
    Cliente básico para hacer peticiones a APIs
    """
    
    def __init__(self, base_url: str = "https://reqres.in/api"):
        self.base_url = base_url
        self.session = requests.Session()
        
    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Método privado para hacer peticiones HTTP
        """
        url = f"{self.base_url}{endpoint}"
        return self.session.request(method, url, **kwargs)
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Realizar petición GET
        """
        return self._make_request("GET", endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Realizar petición POST
        """
        return self._make_request("POST", endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Realizar petición PUT
        """
        return self._make_request("PUT", endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Realizar petición DELETE
        """
        return self._make_request("DELETE", endpoint, **kwargs)

def validar_respuesta_exitosa(response: requests.Response, status_esperado: int = 200):
    """
    Valida que una respuesta HTTP sea exitosa
    """
    assert response.status_code == status_esperado, \
        f"Se esperaba {status_esperado}, se obtuvo {response.status_code}"
    
    # Verificar que la respuesta sea JSON válido
    try:
        response.json()
    except json.JSONDecodeError:
        raise AssertionError("La respuesta no es JSON válido")

def validar_estructura_usuario(usuario: Dict[str, Any]):
    """
    Valida que un usuario tenga la estructura esperada
    """
    campos_requeridos = {"id", "email", "first_name", "last_name", "avatar"}
    campos_usuario = set(usuario.keys())
    
    assert campos_requeridos <= campos_usuario, \
        f"El usuario no tiene todos los campos requeridos. Faltan: {campos_requeridos - campos_usuario}"
    
    # Validaciones específicas
    assert isinstance(usuario["id"], int), "El ID debe ser un entero"
    assert "@" in usuario["email"], "El email debe tener formato válido"
    assert usuario["avatar"].endswith(".jpg"), "El avatar debe terminar en .jpg"

def imprimir_respuesta_detallada(response: requests.Response, titulo: str = "Respuesta API"):
    """
    Imprime detalles de una respuesta HTTP para debugging
    """
    print(f"\n📡 {titulo}")
    print(f"   Status: {response.status_code}")
    print(f"   Headers: {dict(response.headers)}")
    
    try:
        data = response.json()
        print(f"   Body: {json.dumps(data, indent=2, ensure_ascii=False)}")
    except:
        print(f"   Body (texto): {response.text}")

# Ejemplo de uso
if __name__ == "__main__":
    client = APIClient()
    
    # Ejemplo de GET
    response = client.get("/users?page=1")
    imprimir_respuesta_detallada(response, "Lista de usuarios")
    
    # Ejemplo de POST
    payload = {"name": "Test User", "job": "Tester"}
    response = client.post("/users", json=payload)
    imprimir_respuesta_detallada(response, "Usuario creado")