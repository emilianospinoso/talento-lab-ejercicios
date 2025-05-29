import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

@pytest.fixture
def usuario_logueado(driver):
    """Fixture que realiza login antes de cada test de carrito"""
    logger.info("Realizando login previo para tests de carrito")
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login_completo("standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url
    return InventoryPage(driver)

@pytest.mark.ui
@pytest.mark.smoke
def test_agregar_producto_al_carrito(usuario_logueado, driver, request):
    """Test para agregar un producto al carrito"""
    logger.info("=== INICIANDO TEST AGREGAR PRODUCTO ===")
    
    inventory_page = usuario_logueado
    request.node.page_url = driver.current_url
    
    # Obtener contador inicial
    contador_inicial = inventory_page.obtener_contador_carrito()
    
    # Agregar producto
    inventory_page.agregar_primer_producto()
    
    # Verificar incremento
    contador_final = inventory_page.obtener_contador_carrito()
    assert contador_final == contador_inicial + 1
    
    logger.info(f"Carrito actualizado: {contador_inicial} -> {contador_final}")
    logger.info("=== TEST AGREGAR PRODUCTO COMPLETADO ===")

@pytest.mark.ui
def test_agregar_multiples_productos(usuario_logueado, driver, request):
    """Test para agregar múltiples productos"""
    logger.info("=== INICIANDO TEST MÚLTIPLES PRODUCTOS ===")
    
    inventory_page = usuario_logueado
    request.node.page_url = driver.current_url
    
    contador_inicial = inventory_page.obtener_contador_carrito()
    
    # Agregar 3 productos
    for i in range(3):
        inventory_page.agregar_primer_producto()
        contador_actual = inventory_page.obtener_contador_carrito()
        assert contador_actual == contador_inicial + i + 1
        logger.info(f"Producto {i+1} agregado. Total: {contador_actual}")
    
    logger.info("=== TEST MÚLTIPLES PRODUCTOS COMPLETADO ===")