# Instalar dependencias

pip install -r requirements.txt

# Ejecutar todos los tests

pytest tests/test_registro_faker.py -v -s

# Ejecutar solo el test que muestra todos los datos de Faker

pytest tests/test_registro_faker.py::test_datos_faker_completos -v -s

# Ejecutar test con diferentes locales

pytest tests/test_registro_faker.py::test_emails_diferentes_locales -v -s
