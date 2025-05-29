TalentoLab - Framework de Reportes y Logging

Este proyecto implementa un framework completo de testing con reportes HTML y sistema de logging centralizado.

## 🚀 Instalación

# Instalar dependencias

pip install -r requirements.txt

# Verificar instalación

pytest --version
📊 Ejecutar tests y generar reportes
bash# Ejecutar todos los tests con reporte
pytest

# Solo tests de UI

pytest tests/ -v

# Solo tests de API

pytest tests_api/ -v

# Solo tests críticos

pytest -m smoke -v

# Con reintentos automáticos

pytest --reruns 2 --reruns-delay 3
📁 Estructura del proyecto
talentolab_reportes/
├── logs/ # Archivos de log
├── reports/ # Reportes HTML y capturas
├── pages/ # Page Object Model
├── tests/ # Tests de UI (Selenium)
├── tests_api/ # Tests de API (Requests)
├── utils/ # Utilidades y logger
└── conftest.py # Configuración de pytest
📈 Reportes generados

HTML Report: reports/report.html - Reporte visual con capturas
Log File: logs/suite.log - Log detallado de ejecución
Screenshots: reports/screens/ - Capturas automáticas en fallos

🔧 Características

✅ Capturas automáticas en fallos UI
✅ Logging centralizado con timestamps
✅ Reportes HTML autocontenidos
✅ Page Object Model implementado
✅ Tests UI + API integrados
✅ Retry automático en tests flaky

Proyecto desarrollado para TalentoLab
Curso de Automatización de Pruebas

## **Comandos para ejecutar:**

# Navegar a la carpeta

cd talentolab_reportes

# Instalar dependencias

pip install -r requirements.txt

# Ejecutar todos los tests

pytest

# Solo tests de smoke

pytest -m smoke

# Con reintentos

pytest --reruns 2 --reruns-delay 2

# Ver el reporte generado

# Abrir reports/report.html en el navegador

# Ver logs

cat logs/suite.log
