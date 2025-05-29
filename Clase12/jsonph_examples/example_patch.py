import requests
import pytest
import time

URL = 'https://jsonplaceholder.typicode.com/posts/1'

PATCH_PAYLOAD = {'title': 'Título actualizado por PATCH'}

def test_patch_post():
    r = requests.patch(URL, json=PATCH_PAYLOAD)
    assert r.status_code == 200
    body = r.json()
    assert body['title'] == 'Título actualizado por PATCH'
    # El resto de campos se mantienen
    assert 'body' in body
    assert 'userId' in body
    
    print(f"✅ PATCH completado - Solo título actualizado")


# Para ejecutar como script normal
if __name__ == "__main__":
    test_patch_post()
    print("Test completado exitosamente")