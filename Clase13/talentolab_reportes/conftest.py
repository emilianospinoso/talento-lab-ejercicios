import pytest
import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.logger import logger, log_session_start, log_session_end

# Configuración para capturas de pantalla
target = pathlib.Path('reports/screens')
target.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="function")
def driver():
    """Fixture que proporciona un WebDriver configurado con logging"""
    logger.info("Configurando WebDriver...")
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)
    
    logger.info("WebDriver configurado exitosamente")
    
    yield driver
    
    logger.info("Cerrando WebDriver...")
    driver.quit()

# Hook para capturas de pantalla automáticas
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook que se ejecuta después de cada test para capturar pantallas en fallos"""
    outcome = yield
    report = outcome.get_result()

    # Solo capturar en fase 'call' y cuando falla
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Nombre del archivo de captura
            file_name = target / f"{item.name}_{report.when}.png"
            
            try:
                driver.save_screenshot(str(file_name))
                logger.error(f"Captura de pantalla guardada: {file_name}")
                
                # Adjuntar al reporte HTML
                if hasattr(report, 'extra'):
                    report.extra = getattr(report, 'extra', [])
                    report.extra.append({
                        'name': 'screenshot',
                        'format': 'image', 
                        'content': str(file_name)
                    })
            except Exception as e:
                logger.error(f"Error al capturar pantalla: {e}")

# Hooks para personalizar el reporte HTML
def pytest_html_results_table_header(cells):
    """Añade columna 'URL' al reporte HTML"""
    cells.insert(2, 'URL')

def pytest_html_results_table_row(report, cells):
    """Añade la URL de la página al reporte"""
    cells.insert(2, getattr(report, 'page_url', '-'))

# Hooks de sesión
def pytest_sessionstart(session):
    """Se ejecuta al inicio de la sesión de testing"""
    log_session_start()

def pytest_sessionfinish(session, exitstatus):
    """Se ejecuta al final de la sesión de testing"""
    log_session_end()