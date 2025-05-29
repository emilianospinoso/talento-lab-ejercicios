import requests

CREATE_URL = 'https://reqres.in/api/users'

def test_create_user():
    payload = {'name': 'Matias QA', 'job': 'tester'}
    
    r = requests.post(CREATE_URL, json=payload)
    assert r.status_code == 201  # Created
    new_user = r.json()
    assert new_user['name'] == 'Matias QA'
    assert 'id' in new_user and 'createdAt' in new_user
