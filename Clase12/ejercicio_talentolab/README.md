# Navegar a la carpeta del ejercicio

cd ejercicio_talentolab

# Instalar dependencias si es necesario

pip install requests pytest faker

# Ejecutar todos los tests API

pytest tests_api/ -v -s

# Ejecutar solo tests end-to-end

pytest -m e2e -v -s

# Ejecutar solo el test de ciclo de vida

pytest tests_api/test_post_lifecycle.py -v -s

# Ejecutar con reporte HTML

pytest tests_api/ --html=reporte_lifecycle.html --self-contained-html

# Ejecutar test específico

pytest tests_api/test_post_lifecycle.py::test_post_lifecycle_complete -v -s
