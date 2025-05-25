[pytest]
# Marcadores personalizados para organizar tests
markers =
    smoke: pruebas críticas y rápidas que verifican funcionalidad básica
    regression: pruebas de regresión para verificar que no hay retrocesos
    login: pruebas relacionadas con funcionalidad de autenticación
    catalog: pruebas relacionadas con el catálogo de productos
    cart: pruebas relacionadas con funcionalidad del carrito

# Directorios donde buscar tests
testpaths = tests

# Patrones de archivos de test
python_files = test_*.py *_test.py

# Patrones de clases de test
python_classes = Test* *Tests

# Patrones de funciones de test
python_functions = test_*

# Opciones adicionales por defecto
addopts = 
    -v
    --strict-markers
    --strict-config
    --tb=short
    
# Filtros de warnings
filterwarnings =
    ignore::UserWarning
    ignore::DeprecationWarning

# Configuración de logging
log_cli = true
log_cli_level = INFO
log_cli_format = %(asctime)s [%(levelname)8s] %(name)s: %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S