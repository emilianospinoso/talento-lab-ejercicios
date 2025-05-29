import logging
import pathlib
from datetime import datetime

# Crear carpeta de logs si no existe
log_dir = pathlib.Path('logs')
log_dir.mkdir(exist_ok=True)

# Configuración del logger
logging.basicConfig(
    filename=log_dir / 'suite.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s – %(message)s',
    datefmt='%H:%M:%S',
    filemode='a'  # Append mode para no sobrescribir logs anteriores
)

# Logger específico para TalentoLab
logger = logging.getLogger('talentolab')

# También mostrar logs en consola para debugging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%H:%M:%S')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Función para log de inicio de sesión
def log_session_start():
    logger.info("=" * 50)
    logger.info(f"NUEVA SESIÓN DE TESTING - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 50)

# Función para log de fin de sesión  
def log_session_end():
    logger.info("=" * 50)
    logger.info("FIN DE SESIÓN DE TESTING")
    logger.info("=" * 50)