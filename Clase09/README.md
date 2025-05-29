# Refactorización - Automatización con Page Object Model

Este proyecto implementa una automatización de pruebas para el sitio **SauceDemo** utilizando **Selenium WebDriver**, **Python** y el patrón **Page Object Model (POM)**.

## 🎯 Propósito del Proyecto

El objetivo es automatizar los siguientes flujos en la aplicación SauceDemo aplicando mejores prácticas de automatización:

- ✅ Login con credenciales válidas e inválidas
- ✅ Verificación del catálogo de productos
- ✅ Interacción con el carrito de compras (añadir/remover productos)
- ✅ Navegación entre páginas
- ✅ Cierre de sesión

## 🛠️ Tecnologías Utilizadas

- **Python 3.7+**: Lenguaje de programación principal
- **Pytest**: Framework de testing para estructurar y ejecutar pruebas
- **Selenium WebDriver**: Para la automatización de la interfaz web
- **Page Object Model**: Patrón de diseño para mantener código mantenible
- **Git/GitHub**: Para control de versiones

## 🏗️ Arquitectura del Proyecto (Page Object Model)

```
pre-entrega-pom/
├── pages/
│   ├── __init__.py
│   ├── login_page.py      # Page Object para login
│   ├── inventory_page.py  # Page Object para catálogo
│   └── cart_page.py       # Page Object para carrito
├── tests/
│   ├── __init__.py
│   ├── test_login.py      # Tests de autenticación
│   ├── test_catalog.py    # Tests del catálogo
│   └── test_cart.py       # Tests del carrito
├── screenshots/           # Capturas automáticas (generado)
├── conftest.py           # Configuración de pytest y fixtures
├── requirements.txt      # Dependencias del proyecto
├── .gitignore           # Archivos a ignorar por Git
└── README.md            # Documentación del proyecto
```

## 📋 Beneficios del Page Object Model

✅ **Mantenibilidad**: Si cambia la UI, solo se modifica una clase
✅ **Reutilización**: Las acciones se pueden usar en múltiples tests
✅ **Legibilidad**: Los tests son más fáciles de entender
✅ **Escalabilidad**: Fácil agregar nuevas páginas sin afectar las existentes
✅ **Separación de responsabilidades**: Lógica de UI separada de lógica de test

## ⚙️ Instalación y Configuración

### 1. Clonar el repositorio

/_Debes clonar este repositorio_/

### 2. Instalar dependencias

pip install -r requirements.txt

### 3. Configurar WebDriver

- Descargar [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Asegurarse de que esté en el PATH del sistema
- Alternativa: El proyecto usa el Service() automático de Selenium

## ▶️ Ejecución de Tests

### Ejecutar todos los tests

python3 -m pytest -v

### Ejecutar tests por categoría

# Solo tests de login

python3 -m pytest tests/test_login.py -v

# Solo tests del catálogo

python3 -m pytest tests/test_catalog.py -v

# Solo tests del carrito

python3 -m pytest tests/test_cart.py -v

### Ejecutar tests por marcadores

# Solo tests críticos (smoke)

python3 -m pytest -m smoke -v

# Tests de regresión

python3 -m pytest -m regression -v

# Tests específicos de funcionalidad

python3 -m pytest -m login -v
python3 -m pytest -m catalog -v
python3 -m pytest -m cart -v

### Generar reporte HTML

python3 -m pytest --html=reporte.html --self-contained-html -v

### Ejecutar tests en paralelo

python3 -m pytest -n 3 -v # Ejecuta en 3 procesos paralelos

## 🧪 Casos de Prueba Implementados

### 📝 Tests de Login (`test_login.py`)

- `test_login_exitoso_credenciales_validas`: Login exitoso
- `test_login_falla_credenciales_invalidas`: Login con credenciales incorrectas
- `test_login_usuario_bloqueado`: Verificación de usuario bloqueado
- `test_login_multiples_escenarios`: Test parametrizado con múltiples usuarios
- `test_metodo_chaining_login`: Verificación de method chaining

### 📦 Tests de Catálogo (`test_catalog.py`)

- `test_verificar_titulo_pagina_inventario`: Verificación de títulos
- `test_verificar_productos_visibles`: Presencia de productos
- `test_verificar_elementos_interfaz_presentes`: Elementos de UI
- `test_verificar_nombres_productos_esperados`: Productos específicos
- `test_carrito_inicialmente_vacio`: Estado inicial del carrito
- `test_logout_desde_inventario`: Funcionalidad de logout

### 🛒 Tests de Carrito (`test_cart.py`)

- `test_agregar_producto_al_carrito`: Agregar productos
- `test_verificar_producto_en_carrito`: Verificación de contenido
- `test_agregar_multiples_productos`: Múltiples productos
- `test_remover_producto_del_carrito`: Remover productos
- `test_flujo_completo_carrito`: Test de flujo completo
- `test_agregar_diferentes_productos_parametrizado`: Test parametrizado

## 🔧 Fixtures Disponibles

- `driver`: WebDriver configurado con Chrome
- `credenciales_validas`: Usuario y contraseña válidos
- `credenciales_invalidas`: Credenciales incorrectas para testing
- `usuario_bloqueado`: Usuario bloqueado para testing
- `usuario_logueado`: Usuario ya logueado en inventario

## 📸 Funcionalidades Adicionales

- **Capturas automáticas**: Se toman screenshots cuando fallan los tests
- **Marcadores personalizados**: smoke, regression, login, catalog, cart
- **Method chaining**: Sintaxis fluida en Page Objects
- **Fixtures reutilizables**: Para diferentes escenarios de testing
- **Tests parametrizados**: Para probar múltiples escenarios
- **Ejecución paralela**: Soporte para tests concurrentes

## 🚀 Comandos Útiles

# Ejecutar solo tests críticos

python3 -m pytest -m smoke --html=smoke_report.html -v

# Ejecutar con reintento en fallos

python3 -m pytest --reruns 2 --reruns-delay 1 -v

# Ejecutar con timeout

python3 -m pytest --timeout=300 -v

# Ejecutar tests específicos

python3 -m pytest tests/test_login.py::test_login_exitoso_credenciales_validas -v

# Mostrar print statements

python3 -m pytest -s -v

# Ejecutar hasta el primer fallo

python3 -m pytest -x -v

```

## 📊 Estructura de Page Objects

### LoginPage

- Métodos: `abrir()`, `realizar_login()`, `esta_mensaje_error_visible()`
- Encapsula: Campos de usuario/contraseña, botón login, mensajes de error

### InventoryPage

- Métodos: `obtener_productos()`, `agregar_producto_por_indice()`, `ir_al_carrito()`
- Encapsula: Lista de productos, contador del carrito, navegación

### CartPage

- Métodos: `obtener_productos_en_carrito()`, `contiene_producto()`, `continuar_comprando()`
- Encapsula: Productos en carrito, botones de acción, información de productos

## 🏆 Mejores Prácticas Aplicadas

✅ **Locators centralizados** en constantes privadas
✅ **Method chaining** para sintaxis fluida
✅ **Separación clara** entre lógica de página y lógica de test
✅ **Esperas explícitas** en lugar de sleeps
✅ **Fixtures compartidas** para setup común
✅ **Documentación completa** en docstrings
✅ **Manejo de errores** apropiado
✅ **Tests independientes** que no dependen entre sí

## 👤 Autor

[Tu Nombre] - Proyecto de Automatización de Testing

## 📝 Notas

- Este proyecto fue refactorizado aplicando el patrón Page Object Model
- Todos los tests están diseñados para ser independientes y reutilizables
- La estructura permite fácil escalabilidad para nuevas páginas y funcionalidades
- Compatible con CI/CD pipelines
```
