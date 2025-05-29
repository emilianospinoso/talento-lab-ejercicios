from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        """Obtiene el título de la página de inventario"""
        titulo_elemento = self.wait.until(EC.visibility_of_element_located(self._TITLE))
        return titulo_elemento.text

    def obtener_contador_carrito(self):
        """Obtiene el número de productos en el carrito."""
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def agregar_producto_por_nombre(self, nombre_producto):
        """
        Agrega un producto específico al carrito buscándolo por nombre
        """
        productos = self.driver.find_elements(*self._PRODUCTS)
        
        for producto in productos:
            try:
                nombre_elemento = producto.find_element(By.CLASS_NAME, "inventory_item_name")
                if nombre_elemento.text == nombre_producto:
                    boton_agregar = producto.find_element(By.TAG_NAME, "button")
                    boton_agregar.click()
                    return True
            except Exception as e:
                continue
        
        raise Exception(f"No se encontró el producto: {nombre_producto}")

    def agregar_primer_producto(self):
        """Agrega el primer producto disponible al carrito"""
        try:
            primer_boton = self.wait.until(EC.element_to_be_clickable(self._ADD_BUTTONS))
            primer_boton.click()
            return True
        except:
            raise Exception("No se pudo agregar el primer producto")