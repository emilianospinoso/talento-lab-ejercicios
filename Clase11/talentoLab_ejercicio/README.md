# Ejecutar todos los tests

pytest tests/ -v -s

# Ejecutar solo tests de login

pytest tests/test_login_csv.py -v -s

# Ejecutar solo tests de carrito

pytest tests/test_carrito_json.py -v -s

# Ejecutar tests de smoke

pytest -m smoke -v -s
