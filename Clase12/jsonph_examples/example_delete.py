import requests
import pytest
import time

URL = 'https://jsonplaceholder.typicode.com/posts/1'

def test_delete_post():
    r = requests.delete(URL)
    assert r.status_code == 200  # JSONPlaceholder devuelve 200, no 204
    
    # JSONPlaceholder simula la eliminación devolviendo objeto vacío
    body = r.json()
    assert body == {} or 'id' not in body or body['id'] is None
    
    print("✅ DELETE completado - Recurso eliminado")



# Para ejecutar como script normal
if __name__ == "__main__":
    test_delete_post()
    print("Test completado exitosamente")