Guía de Refactorización a Page Object Model - Paso a Paso
Esta guía te llevará desde tu pre-entrega actual hasta una implementación completa del patrón Page Object Model.
Checklist Previo
Antes de comenzar, asegúrate de tener:
✅ Tu pre-entrega original funcionando
✅ Git instalado y configurado
✅ Conocimientos básicos de clases en Python
✅ Selenium y pytest funcionando correctamente
Paso 1: Crear la Estructura de Carpetas
1.1 Crear rama para la refactorización
git checkout -b feature/pom-refactor

1.2 Crear estructura de directorios

# Desde la raíz de tu proyecto

mkdir pages
mkdir tests
touch pages/**init**.py
touch tests/**init**.py

Tu estructura debe quedar así:
pre-entrega-pom/
├── pages/
│ └── **init**.py
├── tests/
│ └── **init**.py
├── conftest.py (ya existe)
├── helpers.py (ya existe, lo vamos a reemplazar)
└── test_saucedemo.py (ya existe, lo vamos a refactorizar)

Paso 2: Crear las Page Objects
2.1 Crear LoginPage
Crea el archivo pages/login_page.py y copia el código completo del LoginPage proporcionado.
Puntos clave del LoginPage:
Locators centralizados como constantes privadas (\_USERNAME_INPUT)
Métodos específicos para cada acción (ingresar_usuario, ingresar_password)
Method chaining (cada método retorna self)
Verificaciones sin asserts (retornan boolean)
2.2 Crear InventoryPage
Crea el archivo pages/inventory_page.py y copia el código completo del InventoryPage proporcionado.
Puntos clave del InventoryPage:
Encapsula toda la interacción con la página de productos
Métodos para obtener información (obtener_cantidad_productos)
Métodos para realizar acciones (agregar_producto_por_indice)
Navegación a otras páginas (ir_al_carrito, realizar_logout)
2.3 Crear CartPage
Crea el archivo pages/cart_page.py y copia el código completo del CartPage proporcionado.
Puntos clave del CartPage:
Verifica automáticamente que estamos en la página correcta
Métodos para obtener información de productos en el carrito
Navegación de regreso al inventario
2.4 Actualizar init.py de pages
Actualiza pages/**init**.py con las importaciones necesarias.
Paso 3: Actualizar conftest.py
3.1 Analizar tu conftest.py actual
Compara tu conftest.py actual con la versión POM proporcionada.
3.2 Agregar nuevas fixtures
Las nuevas fixtures importantes son:
credenciales_validas: Para tests parametrizados
credenciales_invalidas: Para tests de fallo
usuario_bloqueado: Para casos especiales
3.3 Mejorar la fixture driver
Asegúrate de que tu fixture driver tenga:
Configuraciones de Chrome optimizadas
Manejo apropiado de cleanup
Scope correcto (function vs session)
Paso 4: Refactorizar Tests Existentes
4.1 Mapear tests actuales a nuevos archivos
Del archivo original test_saucedemo.py a:
test_login_success → tests/test_login.py
test_verify_catalog → tests/test_catalog.py
test_cart_functionality → tests/test_cart.py
Tests adicionales → Distribuir según funcionalidad
4.2 Refactorizar test de login
ANTES (estilo directo):
def test_login_success(driver):
driver.get("https://www.saucedemo.com/")
username_input = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "user-name"))
)
username_input.send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click() # verificaciones...

DESPUÉS (estilo POM):
def test_login_exitoso_credenciales_validas(driver, credenciales_validas):
login_page = LoginPage(driver)
login_page.abrir().realizar_login(
credenciales_validas["usuario"],
credenciales_validas["password"]
)

    inventory_page = InventoryPage(driver)
    assert inventory_page.esta_en_pagina_inventario()

4.3 Refactorizar test de catálogo
Transformación clave:
Extraer todas las interacciones con elementos a InventoryPage
Usar fixture usuario_logueado para tests que requieren login previo
Separar verificaciones en múltiples tests específicos
4.4 Refactorizar test de carrito
Transformación clave:
Usar métodos específicos como agregar_primer_producto()
Navegar entre páginas usando los Page Objects
Verificar estado usando métodos como contiene_producto()
Paso 5: Agregar Tests Adicionales
5.1 Tests parametrizados
Agrega tests parametrizados para cubrir múltiples escenarios:
@pytest.mark.parametrize("usuario,password,deberia_funcionar", [
("standard_user", "secret_sauce", True),
("locked_out_user", "secret_sauce", False),
# más casos...
])

5.2 Tests de flujo completo
Agrega tests que cubran flujos completos end-to-end.
5.3 Tests de regresión
Marca tests importantes como @pytest.mark.regression.
Paso 6: Configurar Marcadores y pytest.ini
6.1 Crear pytest.ini
Crea el archivo pytest.ini en la raíz del proyecto con la configuración proporcionada.
6.2 Aplicar marcadores a tus tests
Agrega marcadores a tus tests:
@pytest.mark.smoke # Tests críticos
@pytest.mark.login # Tests de funcionalidad específica
def test_login_exitoso_credenciales_validas(driver, credenciales_validas): # test code...

6.3 Verificar marcadores
pytest --markers # Ver todos los marcadores disponibles

Paso 7: Ejecutar y Verificar
7.1 Ejecutar tests individuales

# Test individual

pytest tests/test_login.py::test_login_exitoso_credenciales_validas -v

# Por archivo

pytest tests/test_login.py -v

7.2 Ejecutar por marcadores

# Tests críticos

pytest -m smoke -v

# Tests de login

pytest -m login -v

7.3 Ejecutar todos los tests
pytest -v

7.4 Generar reporte
pytest --html=reporte_pom.html --self-contained-html -v

Paso 8: Verificación de Calidad
8.1 Checklist de Page Objects
✅ Locators centralizados y privados
✅ Métodos con nombres descriptivos
✅ Method chaining implementado
✅ Sin asserts dentro de las páginas
✅ Navegación entre páginas retorna Page Objects
8.2 Checklist de Tests
✅ Tests legibles y específicos
✅ Uso de fixtures apropiadas
✅ Marcadores aplicados correctamente
✅ Tests independientes entre sí
✅ Documentación completa (docstrings)
8.3 Verificar eliminación de duplicación
✅ No hay selectores duplicados entre tests
✅ Acciones comunes centralizadas
✅ Setup común en fixtures
Paso 9: Actualizar Documentación
9.1 Actualizar README.md
Reemplaza tu README.md con la versión POM proporcionada, personalizando:
Tu nombre como autor
URL de tu repositorio
Cualquier instrucción específica
9.2 Crear requirements.txt
Crea el archivo requirements.txt con las dependencias especificadas.
9.3 Actualizar .gitignore
Asegúrate de que tu .gitignore incluya:
**pycache**/
_.pyc
.pytest_cache/
screenshots/
_.html
assets/

Paso 10: Commit y Push
10.1 Revisar cambios
git status
git diff

10.2 Hacer commit por partes

# Agregar structure

git add pages/ tests/ pytest.ini requirements.txt
git commit -m "feat: implement Page Object Model structure"

# Agregar tests refactorizados

git add tests/
git commit -m "refactor: migrate tests to POM pattern"

# Actualizar documentación

git add README.md conftest.py
git commit -m "docs: update documentation for POM implementation"

10.3 Push de la rama
git push origin feature/pom-refactor

Paso 11: Validación Final
11.1 Prueba completa

# Ejecutar suite completa

pytest -v

# Ejecutar con reporte

pytest --html=reporte_final.html -v

# Verificar tests críticos

pytest -m smoke -v

11.2 Verificar beneficios logrados
Antes del POM:
Cambiar un selector requería editar múltiples archivos
Tests difíciles de leer y mantener
Código duplicado en diferentes tests
Lógica de UI mezclada con lógica de test
Después del POM:
✅ Un selector se cambia en un solo lugar
✅ Tests legibles que cuentan historias de usuario
✅ Código reutilizable y centralizado
✅ Separación clara de responsabilidades
🏆 Paso 12: Crear Pull Request
12.1 Crear PR descriptivo
Título: feat: Implement Page Object Model pattern for test automation
Descripción:

## 🎯 Objetivo

Refactorizar la suite de tests aplicando el patrón Page Object Model para mejorar mantenibilidad y escalabilidad.

## 🔧 Cambios Realizados

- ✅ Creada estructura de carpetas pages/ y tests/
- ✅ Implementados Page Objects para Login, Inventory y Cart
- ✅ Refactorizados tests existentes al patrón POM
- ✅ Agregados tests adicionales con parametrización
- ✅ Configurados marcadores y pytest.ini
- ✅ Actualizada documentación completa

## 🧪 Tests

- [x] Todos los tests pasan
- [x] Tests organizados por funcionalidad
- [x] Marcadores aplicados correctamente
- [x] Reporte HTML generado

## 📋 Checklist

- [x] Page Objects siguen convenciones establecidas
- [x] Tests son independientes y reutilizables
- [x] Documentación actualizada
- [x] Requirements.txt actualizado

¡Felicitaciones!
Has completado exitosamente la refactorización a Page Object Model. Tu código ahora es:
🔧 Más mantenible: Cambios de UI se hacen en un solo lugar
📖 Más legible: Tests que cuentan historias claras
🔄 Más reutilizable: Componentes que se pueden usar en múltiples tests
📈 Más escalable: Fácil agregar nuevas páginas y funcionalidades
Próximos Pasos
Merge del PR: Una vez aprobado, hacer merge a main
Continuous Integration: Configurar CI/CD con GitHub Actions
Más Page Objects: Agregar páginas adicionales (Checkout, Profile, etc.)
Data-Driven Testing: Implementar tests con archivos CSV/JSON
Reporting avanzado: Agregar Allure o reportes más detallados
Tips para el Futuro
Mantén los Page Objects simples: Un método por acción
Usa method chaining: Para sintaxis más fluida
Documenta bien: Cada método debe tener docstring clara
Tests atómicos: Cada test debe probar una sola cosa
Fixtures específicas: Crea fixtures para casos específicos
Revisión constante: Refactoriza cuando agregues nuevas funcionalidades
