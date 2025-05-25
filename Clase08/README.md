# Clase 08 – Selenium: Login y Carrito (SauceDemo)

Este script automatiza el flujo básico de login en [saucedemo.com](https://www.saucedemo.com), valida el acceso correcto, agrega un producto al carrito y verifica que el contador del carrito sea 1.

---

## ¿Qué valida?

- Acceso con credenciales válidas (`standard_user` / `secret_sauce`)
- Redirección a `/inventory.html`
- Presencia del texto “Products”
- Agregado del primer producto al carrito
- Visualización del contador de carrito con valor `1`
- Verificación opcional del producto dentro del carrito
- Resultado esperado: **`Test OK`** en consola

## Cómo ejecutarlo

1. Instalá Selenium si aún no lo hiciste:
   pip install selenium

Asegurate de tener Chrome instalado y el chromedriver correspondiente en tu PATH.

Ejecutá el script:
python3 test_login_carrito.py
Si todo funciona correctamente, verás:

Test OK
Y el navegador se cerrará automáticamente.
