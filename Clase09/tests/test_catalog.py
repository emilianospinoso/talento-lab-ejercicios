"""
Tests para la funcionalidad del catálogo/inventario usando Page Object Model.
Incluye verificaciones de productos, interfaz y navegación.
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def usuario_logueado(driver, credenciales_validas):
    """
    Fixture que proporciona un usuario ya logueado en la página de inventario.
    
    Returns:
        InventoryPage: Instancia de la página de inventario con usuario logueado
    """
    # Realizar login
    login_page = LoginPage(driver)
    login_page.abrir().realizar_login(
        credenciales_validas["usuario"], 
        credenciales_validas["password"]
    )
    
    # Retornar instancia de inventory page
    return InventoryPage(driver)


@pytest.mark.smoke
@pytest.mark.catalog
def test_verificar_titulo_pagina_inventario(usuario_logueado):
    """
    Verifica que el título de la página de inventario sea correcto.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Verificar título del navegador
    3. Verificar título de la página
    """
    inventory_page = usuario_logueado
    
    # Verificar título del navegador
    titulo_navegador = inventory_page.obtener_titulo_navegador()
    assert titulo_navegador == "Swag Labs", f"Título del navegador incorrecto: {titulo_navegador}"
    
    # Verificar título de la página
    titulo_pagina = inventory_page.obtener_titulo_pagina()
    assert titulo_pagina == "Products", f"Título de la página incorrecto: {titulo_pagina}"
    
    print("✅ Títulos de página verificados correctamente")


@pytest.mark.smoke
@pytest.mark.catalog
def test_verificar_productos_visibles(usuario_logueado):
    """
    Verifica que haya productos visibles en la página de inventario.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Obtener lista de productos
    3. Verificar que hay al menos un producto
    4. Verificar que los productos tienen nombres
    """
    inventory_page = usuario_logueado
    
    # Verificar que hay productos
    cantidad_productos = inventory_page.obtener_cantidad_productos()
    assert cantidad_productos > 0, "No hay productos visibles en la página"
    
    # Verificar que los productos tienen nombres
    nombres_productos = inventory_page.obtener_nombres_productos()
    assert len(nombres_productos) == cantidad_productos, "No todos los productos tienen nombres"
    assert all(nombre.strip() for nombre in nombres_productos), "Algunos productos tienen nombres vacíos"
    
    print(f"✅ Se encontraron {cantidad_productos} productos con nombres válidos")


@pytest.mark.catalog
def test_verificar_elementos_interfaz_presentes(usuario_logueado):
    """
    Verifica que los elementos importantes de la interfaz estén presentes.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Verificar presencia del dropdown de filtros
    3. Verificar presencia del menú hamburguesa
    4. Verificar presencia del ícono del carrito
    """
    inventory_page = usuario_logueado
    
    # Verificar dropdown de filtros
    assert inventory_page.esta_dropdown_filtro_presente(), "Dropdown de filtros no encontrado"
    
    # Verificar menú hamburguesa
    assert inventory_page.esta_menu_presente(), "Menú hamburguesa no encontrado"
    
    # Verificar ícono del carrito
    assert inventory_page.esta_icono_carrito_presente(), "Ícono del carrito no encontrado"
    
    print("✅ Todos los elementos de la interfaz están presentes")


@pytest.mark.catalog
def test_verificar_nombres_productos_esperados(usuario_logueado):
    """
    Verifica que algunos productos específicos esperados estén presentes.
    
    Este test valida que ciertos productos conocidos de SauceDemo estén en el catálogo.
    """
    inventory_page = usuario_logueado
    
    # Obtener nombres de productos
    nombres_productos = inventory_page.obtener_nombres_productos()
    
    # Productos que esperamos encontrar (lista parcial)
    productos_esperados = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt"
    ]
    
    # Verificar que al menos algunos productos esperados estén presentes
    productos_encontrados = [producto for producto in productos_esperados if producto in nombres_productos]
    
    assert len(productos_encontrados) > 0, f"No se encontraron productos esperados. Productos disponibles: {nombres_productos}"
    
    print(f"✅ Productos esperados encontrados: {productos_encontrados}")


@pytest.mark.catalog
def test_carrito_inicialmente_vacio(usuario_logueado):
    """
    Verifica que el carrito esté inicialmente vacío cuando se accede al inventario.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Verificar que el contador del carrito sea 0
    3. Verificar que el carrito esté marcado como vacío
    """
    inventory_page = usuario_logueado
    
    # Verificar que el contador del carrito sea 0
    contador_carrito = inventory_page.obtener_contador_carrito()
    assert contador_carrito == 0, f"El carrito debería estar vacío pero tiene {contador_carrito} productos"
    
    # Verificar usando el método de verificación
    assert inventory_page.esta_carrito_vacio(), "El carrito no está marcado como vacío"
    
    print("✅ Carrito inicialmente vacío verificado")


@pytest.mark.regression
@pytest.mark.catalog
def test_cantidad_minima_productos(usuario_logueado):
    """
    Test de regresión que verifica que hay una cantidad mínima de productos.
    
    SauceDemo normalmente tiene 6 productos, este test asegura que no haya regresiones.
    """
    inventory_page = usuario_logueado
    
    cantidad_productos = inventory_page.obtener_cantidad_productos()
    
    # SauceDemo normalmente tiene 6 productos
    CANTIDAD_MINIMA_ESPERADA = 6
    
    assert cantidad_productos >= CANTIDAD_MINIMA_ESPERADA, \
        f"Se esperaban al menos {CANTIDAD_MINIMA_ESPERADA} productos, pero se encontraron {cantidad_productos}"
    
    print(f"✅ Cantidad de productos cumple con el mínimo esperado: {cantidad_productos}")


@pytest.mark.catalog
def test_logout_desde_inventario(usuario_logueado):
    """
    Verifica que se pueda hacer logout desde la página de inventario.
    
    Pasos:
    1. Usuario ya logueado (fixture)
    2. Realizar logout
    3. Verificar redirección a página de login
    """
    inventory_page = usuario_logueado
    
    # Realizar logout
    login_page = inventory_page.realizar_logout()
    
    # Verificar que estamos en la página de login
    assert login_page.esta_en_pagina_login(), "No se redirigió correctamente a la página de login"
    
    print("✅ Logout desde inventario completado correctamente")