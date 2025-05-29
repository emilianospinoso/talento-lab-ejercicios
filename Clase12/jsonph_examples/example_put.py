import requests
import pytest
import time

URL = 'https://jsonplaceholder.typicode.com/posts/1'

payload = {
    'id': 1,
    'title': 'Automation Testing Guide',
    'body': 'Guía completa de testing automatizado',
    'userId': 1
}

def test_put_post():
    start = time.time()
    r = requests.put(URL, json=payload)
    assert r.status_code == 200
    body = r.json()
    assert body['title'] == 'Automation Testing Guide'
    assert body['body'] == 'Guía completa de testing automatizado'
    assert body['id'] == 1
    assert r.elapsed.total_seconds() < 1
    
    print(f"✅ PUT completado en {r.elapsed.total_seconds():.3f}s")

# Para ejecutar como script normal
if __name__ == "__main__":
    test_put_post()
    print("Test completado exitosamente")