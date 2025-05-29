# Clase 11: Automatización de Pruebas de API - Parte 1

Este repositorio contiene los ejercicios y ejemplos de la Clase 11 del curso de Automatización de Pruebas.

## 📁 Estructura del proyecto

Clase11/
├── reqres_example/ # Ejemplos básicos con reqres.in
│ ├── test01.py # Primer ejemplo con GitHub API
│ ├── test02.py # GET request - listar usuarios
│ ├── test03.py # POST request - crear usuario
│ └── test04.py # POST request - login
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
