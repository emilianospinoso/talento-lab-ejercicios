import requests

# 1) Hacemos la solicitud HTTP
resp = requests.get('https://api.github.com/')

# 2) Imprimimos el código de estado
print(resp.status_code)  # 200 = OK

# 3) Vemos el tipo de contenido devuelto
print(resp.headers['content-type'])  # application/json

# 4) Convertimos el JSON a dict de Python  
payload = resp.json()
print(payload['current_user_url'])
