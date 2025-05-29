from selenium import webdriver
import logging
logger = logging.getLogger('talentolab')

# --- HOOKS ---
def before_all(context):
    """Arranca el navegador y pone tiempo de espera implícito."""
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)  # evita sleeps fijos



def before_scenario(context, scenario):
    logger.info('▶️ Iniciando escenario: %s', scenario.name)
