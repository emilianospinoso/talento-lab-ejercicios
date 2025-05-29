from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pathlib
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('behave')

# Carpeta para capturas de pantalla
SCREEN_DIR = pathlib.Path('reports/screens')
SCREEN_DIR.mkdir(parents=True, exist_ok=True)

def before_all(context):
    """Se ejecuta una vez antes de todas las features"""
    logger.info("=== INICIANDO SUITE DE BDD ===")
    
    # Configurar Chrome
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    
    service = Service()
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.implicitly_wait(5)
    
    logger.info("WebDriver configurado exitosamente")

def before_scenario(context, scenario):
    """Se ejecuta antes de cada scenario"""
    logger.info(f"▶️ Iniciando escenario: {scenario.name}")

def after_step(context, step):
    """Se ejecuta después de cada step"""
    if step.status == 'failed' and hasattr(context, 'driver'):
        # Capturar screenshot en caso de fallo
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{step.name.replace(' ', '_')}_{timestamp}.png"
        filepath = SCREEN_DIR / filename
        
        try:
            context.driver.save_screenshot(str(filepath))
            logger.error(f"Screenshot guardado: {filepath}")
        except Exception as e:
            logger.error(f"Error al guardar screenshot: {e}")

def after_scenario(context, scenario):
    """Se ejecuta después de cada scenario"""
    if scenario.status == 'failed':
        logger.error(f"❌ Escenario falló: {scenario.name}")
    else:
        logger.info(f"✅ Escenario exitoso: {scenario.name}")

def after_all(context):
    """Se ejecuta una vez después de todas las features"""
    if hasattr(context, 'driver'):
        context.driver.quit()
        logger.info("WebDriver cerrado")
    
    logger.info("=== SUITE DE BDD FINALIZADA ===")