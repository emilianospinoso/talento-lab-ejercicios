Ejemplos de BDD con Behave - Clase 14

Este directorio contiene los ejemplos prácticos de la Clase 14 sobre Behavior-Driven Development.

## 🚀 Instalación

pip install -r requirements.txt
📋 Ejecutar ejemplos

# Todos los ejemplos

behave

# Solo tests unitarios

behave -t @unit

# Solo tests de UI

behave -t @ui

# Solo tests de API

behave -t @api

# Tests de smoke

behave -t @smoke

# Con reporte HTML

behave -f html -o reports/behave.html
📁 Estructura

features/: Archivos .feature con scenarios en Gherkin
features/steps/: Step definitions en Python
features/environment.py: Hooks globales
utils/: Código a testear
pages/: Page Objects para UI tests

🎯 Ejemplos incluidos

Operaciones matemáticas - Tests unitarios puros
Login SauceDemo - Tests de UI con Selenium
API JSONPlaceholder - Tests de API con Requests
