import requests
import pytest

URL = 'https://reqres.in/api/users?page=2'

def test_get_users():
    r = requests.get(URL)
    assert r.status_code == 200
    data = r.json()
    assert data['page'] == 2
    assert len(data['data']) > 0  # al menos un usuario
