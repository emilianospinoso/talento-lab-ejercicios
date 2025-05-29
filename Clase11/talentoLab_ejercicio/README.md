# Clase 11: Automatización de Pruebas de API - Parte 1

Este repositorio contiene los ejercicios y ejemplos de la Clase 11 del curso de Automatización de Pruebas.

## 📁 Estructura del proyecto

Clase11/
├── talentoLab_ejercicio/ # Ejercicio principal de TalentoLab
│ ├── datos/ # Archivos de datos (CSV/JSON)
│ ├── pages/ # Page Object Model para UI
│ ├── tests/ # Tests de UI (Selenium)
│ ├── tests_api/ # Tests de API (Requests)
│ ├── utils/ # Utilidades compartidas
│ ├── conftest.py # Fixtures de pytest
│ └── pytest.ini # Configuración de pytest
└── README.md

## 🚀 Instalación y configuración

### Prerequisitos

- Python 3.8+
- Chrome/Chromium instalado
- ChromeDriver configurado

### Instalar dependencias

pip install requests selenium pytest faker pytest-html

📋 Ejemplos básicos (reqres_example/)
Ejecutar ejemplos individuales
bash# Ejemplo 1: GitHub API
python3 test01.py

# Ejemplo 2: GET usuarios

python3 test02.py

# Ejemplo 3: POST crear usuario

python3 test03.py

# Ejemplo 4: POST login

python3 test04.py
Ejecutar con pytest
bashcd reqres_example/
pytest test02.py test03.py test04.py -v
🧪 Ejercicio TalentoLab (talentoLab_ejercicio/)
Ejecutar tests de UI (Selenium)
bashcd talentoLab_ejercicio/

# Todos los tests UI

pytest tests/ -v -s

# Solo login

pytest tests/test_login_csv.py -v -s

# Solo carrito

pytest tests/test_carrito_json.py -v -s

# Tests de smoke

pytest -m smoke -v -s
Ejecutar tests de API (Requests)
bash# Todos los tests API
pytest tests_api/ -v -s

# Solo tests API con marca específica

pytest -m api -v -s

# Test específico

pytest tests_api/test_login_api.py -v -s
Ejecutar todo junto (UI + API)
bash# Todos los tests
pytest tests/ tests_api/ -v

# Solo tests de smoke (UI + API)

pytest -m smoke -v

# Generar reporte HTML completo

pytest tests/ tests_api/ --html=reporte_completo.html --self-contained-html
📊 Tipos de tests
Tests de UI (Selenium)

Login parametrizado: Múltiples usuarios desde CSV
Carrito de compras: Agregar productos desde JSON
Page Object Model: Estructura organizada y mantenible

Tests de API (Requests)

Login API: Autenticación con diferentes credenciales
Usuarios API: Listar y obtener usuarios individuales
Crear usuarios: POST con datos fijos y aleatorios (Faker)

🏷️ Markers de pytest
bash# Solo tests de API
pytest -m api

# Solo tests de UI

pytest -m ui

# Tests de smoke (críticos)

pytest -m smoke

# Tests de manejo de errores

pytest -m exception
📈 Reportes
Reporte HTML básico
bashpytest --html=reporte.html --self-contained-html
Reporte completo (UI + API)
bashpytest tests/ tests_api/ --html=reporte_completo.html --self-contained-html
