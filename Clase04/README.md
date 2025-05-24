# instalar dependencias (una sola vez)

pip install pytest pytest-html

# suite completa, verbosa

pytest -v

# solo los tests “sumar” (smoke)

pytest -v -m smoke

# solo los tests que validan la excepción de división

pytest -v -m exception

# reporte HTML autosuficiente

pytest --html=report.html --self-contained-html
El archivo report.html queda listo para adjuntar en tu Pull Request. ¡Suite preparada y objetivos de la Clase 04 cumplidos!
