"""
Configuración global de pytest para el proyecto de automatización.
Contiene fixtures compartidas y configuraciones para todos los tests.
"""

import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_configure(config):
    """
    Configuración que se ejecuta al iniciar pytest.
    Crea el directorio para capturas de pantalla si no existe.
    """
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
        print("Directorio 'screenshots' creado.")


@pytest.fixture(scope="function")
def driver():
    """
    Fixture que proporciona una instancia de Chrome WebDriver configurada.
    Se ejecuta antes de cada test y se limpia después.
    
    Yields:
        WebDriver: Instancia del driver de Chrome configurada
    """
    # Configuración del driver de Chrome
    chrome_options = Options()
    
    # Opciones para mejorar la estabilidad
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Descomenta la siguiente línea para ejecutar en modo headless (sin interfaz gráfica)
    # chrome_options.add_argument("--headless")
    
    # Inicializar el servicio y el driver
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Configuraciones adicionales del driver
    driver.maximize_window()
    driver.implicitly_wait(5)  # Espera implícita de 5 segundos
    
    # Proporcionar el driver al test
    yield driver
    
    # Limpieza después del test
    driver.quit()


@pytest.fixture
def credenciales_validas():
    """
    Fixture que proporciona credenciales válidas para SauceDemo.
    
    Returns:
        dict: Diccionario con usuario y contraseña válidos
    """
    return {
        "usuario": "standard_user",
        "password": "secret_sauce"
    }


@pytest.fixture
def credenciales_invalidas():
    """
    Fixture que proporciona credenciales inválidas para testing.
    
    Returns:
        dict: Diccionario con usuario y contraseña inválidos
    """
    return {
        "usuario": "invalid_user",
        "password": "invalid_password"
    }


@pytest.fixture
def usuario_bloqueado():
    """
    Fixture que proporciona credenciales de un usuario bloqueado.
    
    Returns:
        dict: Diccionario con usuario bloqueado y contraseña válida
    """
    return {
        "usuario": "locked_out_user",
        "password": "secret_sauce"
    }


# Hook para tomar capturas de pantalla cuando un test falla
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de pytest que captura screenshots cuando un test falla.
    """
    # Ejecutar todas las demás hooks para obtener el resultado
    outcome = yield
    rep = outcome.get_result()
    
    # Verificamos si estamos en la fase de call y si ha fallado el test
    if rep.when == "call" and rep.failed:
        # Intentamos obtener el driver desde la fixture
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"failure_{item.name}_{timestamp}.png"
            try:
                driver.save_screenshot(f"screenshots/{screenshot_name}")
                print(f"\n📸 Captura de pantalla guardada: {screenshot_name}")
            except Exception as e:
                print(f"\n❌ Error al guardar captura de pantalla: {e}")


# Marcadores personalizados para pytest
def pytest_configure(config):
    """Registra marcadores personalizados para evitar warnings."""
    config.addinivalue_line(
        "markers", "smoke: marca tests como pruebas de smoke (críticas y rápidas)"
    )
    config.addinivalue_line(
        "markers", "regression: marca tests como pruebas de regresión"
    )
    config.addinivalue_line(
        "markers", "login: marca tests relacionados con funcionalidad de login"
    )
    config.addinivalue_line(
        "markers", "cart: marca tests relacionados con funcionalidad del carrito"
    )
    config.addinivalue_line(
        "markers", "catalog: marca tests relacionados con el catálogo de productos"
    )