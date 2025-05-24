# test_login_carrito.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar Chrome
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

try:
    # 1) Abrir la página de login
    driver.get("https://www.saucedemo.com/")

    # 2) Completar usuario y contraseña
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 3) Hacer clic en login
    driver.find_element(By.ID, "login-button").click()

    # 4) Validar login exitoso
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url

    header = driver.find_element(By.CLASS_NAME, "title").text
    assert "Products" in header

    # 5) Agregar el primer producto al carrito
    driver.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-cart')]").click()

    # 6) Esperar badge y verificar que sea 1
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"

    # 7) (Opcional) Ingresar al carrito y verificar el producto
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    print("Test OK")

finally:
    driver.quit()
