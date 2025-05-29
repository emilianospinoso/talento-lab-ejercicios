import requests

LOGIN_URL = 'https://reqres.in/api/login'
def test_login_successful():
    creds = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    resp = requests.post(LOGIN_URL, json=creds)
    
    assert resp.status_code == 200
    assert 'token' in resp.json()
