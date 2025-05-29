import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger

@pytest.mark.ui
@pytest.mark.smoke
def test_login_exitoso(driver, request):
    """Test de login exitoso con logging y captura de URL"""
    logger.info("=== INICIANDO TEST DE LOGIN EXITOSO ===")
    
    login_page = LoginPage(driver)
    login_page.abrir()
    
    # Capturar URL para el reporte
    request.node.page_url = driver.current_url
    
    login_page.login_completo("standard_user", "secret_sauce")
    
    # Verificar redirección
    assert "inventory.html" in driver.current_url
    request.node.page_url = driver.current_url
    
    # Verificar título
    inventory_page = InventoryPage(driver)
    titulo = inventory_page.obtener_titulo()
    assert titulo == "Products"
    
    logger.info("=== TEST DE LOGIN EXITOSO COMPLETADO ===")

@pytest.mark.ui
def test_login_fallido(driver, request):
    """Test de login fallido con credenciales incorrectas"""
    logger.info("=== INICIANDO TEST DE LOGIN FALLIDO ===")
    
    login_page = LoginPage(driver)
    login_page.abrir()
    
    request.node.page_url = driver.current_url
    
    login_page.login_completo("usuario_malo", "password_malo")
    
    # Verificar que aparece error
    assert login_page.esta_error_visible()
    mensaje_error = login_page.obtener_mensaje_error()
    assert len(mensaje_error) > 0
    
    logger.info(f"Error esperado mostrado: {mensaje_error}")
    logger.info("=== TEST DE LOGIN FALLIDO COMPLETADO ===")

@pytest.mark.ui
def test_login_usuario_bloqueado(driver, request):
    """Test con usuario bloqueado"""
    logger.info("=== INICIANDO TEST DE USUARIO BLOQUEADO ===")
    
    login_page = LoginPage(driver)
    login_page.abrir()
    
    request.node.page_url = driver.current_url
    
    login_page.login_completo("locked_out_user", "secret_sauce")
    
    # Verificar que aparece error
    assert login_page.esta_error_visible()
    mensaje_error = login_page.obtener_mensaje_error()
    assert "locked out" in mensaje_error.lower()
    
    logger.info("=== TEST DE USUARIO BLOQUEADO COMPLETADO ===")