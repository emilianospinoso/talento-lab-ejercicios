# 🧪 Clase 07 – Selenium WebDriver

En esta clase damos el primer paso serio en automatización UI: escribir nuestros propios scripts Selenium para interactuar con la web como si fuéramos usuarios reales.

## 🎯 Objetivos

- Instalar y configurar Selenium + WebDriver.
- Automatizar el login en SauceDemo.
- Validar visualmente la sección de inventario.
- Interactuar con el carrito de compras.
- Utilizar los selectores definidos en la Clase 06.
- Imprimir `Test OK` si el flujo se completa correctamente.

## ⚙️ Requisitos

- Python 3 instalado.
- Selenium 4:
  pip install selenium
  Chrome instalado (ej. versión 133).

ChromeDriver descargado con la misma versión que tu navegador:
Descargar desde [aquí](https://googlechromelabs.github.io/chrome-for-testing/)

Verificá que ChromeDriver esté en tu PATH o en la misma carpeta que los scripts:

chromedriver --version
🚀 Cómo ejecutar los scripts
Asegurate de estar en la carpeta Clase07

Desde la terminal ejecutá:

python3 actividad_1_login.py
python3 actividad_2_inventario.py
python3 actividad_3_carrito.py
