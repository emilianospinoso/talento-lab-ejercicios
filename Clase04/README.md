# instalar dependencias (una sola vez)

pip install pytest pytest-html

# suite completa, verbosa

Dentro de Clase04 ejecuta:
python3 -m pytest -v

# solo los tests “sumar” (smoke)

python3 -m pytest -v -m smoke

# solo los tests que validan la excepción de división

python3 -m pytest -v -m exception

# reporte HTML autosuficiente

python3 -m pytest --html=report.html --self-contained-html
El archivo report.html queda listo para adjuntar en tu Pull Request. ¡Suite preparada y objetivos de la Clase 04 cumplidos!
