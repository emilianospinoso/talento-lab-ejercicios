"""
Page Object para la página del carrito de compras de SauceDemo.
Encapsula todos los elementos y acciones relacionadas con el carrito.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Representa la página del carrito de compras de SauceDemo.
    Proporciona métodos para interactuar con los productos del carrito.
    """
    
    # Localizadores de elementos
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")
    _ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    _REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='remove']")
    _CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    _CHECKOUT_BUTTON = (By.ID, "checkout")
    _CART_TITLE = (By.CLASS_NAME, "title")
    
    def __init__(self, driver):
        """
        Inicializa la página del carrito con el driver proporcionado.
        Verifica que estemos en la página correcta.
        
        Args:
            driver: Instancia del WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Verificar que estamos en la página del carrito
        self.wait.until(EC.url_contains("cart.html"))
    
    def obtener_titulo_pagina(self):
        """
        Obtiene el título de la página del carrito.
        
        Returns:
            str: Título de la página del carrito
        """
        return self.driver.find_element(*self._CART_TITLE).text
    
    def obtener_productos_en_carrito(self):
        """
        Obtiene la lista de elementos de productos en el carrito.
        
        Returns:
            list: Lista de elementos WebElement que representan productos en el carrito
        """
        return self.driver.find_elements(*self._CART_ITEMS)
    
    def obtener_cantidad_productos(self):
        """
        Obtiene la cantidad de productos en el carrito.
        
        Returns:
            int: Número de productos en el carrito
        """
        return len(self.obtener_productos_en_carrito())
    
    def obtener_nombres_productos(self):
        """
        Obtiene los nombres de todos los productos en el carrito.
        
        Returns:
            list: Lista con los nombres de los productos en el carrito
        """
        elementos_nombres = self.driver.find_elements(*self._ITEM_NAMES)
        return [elemento.text for elemento in elementos_nombres]
    
    def obtener_descripciones_productos(self):
        """
        Obtiene las descripciones de todos los productos en el carrito.
        
        Returns:
            list: Lista con las descripciones de los productos
        """
        elementos_descripciones = self.driver.find_elements(*self._ITEM_DESCRIPTIONS)
        return [elemento.text for elemento in elementos_descripciones]
    
    def obtener_precios_productos(self):
        """
        Obtiene los precios de todos los productos en el carrito.
        
        Returns:
            list: Lista con los precios de los productos
        """
        elementos_precios = self.driver.find_elements(*self._ITEM_PRICES)
        return [elemento.text for elemento in elementos_precios]
    
    def esta_carrito_vacio(self):
        """
        Verifica si el carrito está vacío.
        
        Returns:
            bool: True si el carrito está vacío, False en caso contrario
        """
        return self.obtener_cantidad_productos() == 0
    
    def contiene_producto(self, nombre_producto):
        """
        Verifica si un producto específico está en el carrito.
        
        Args:
            nombre_producto (str): Nombre del producto a buscar
            
        Returns:
            bool: True si el producto está en el carrito, False en caso contrario
        """
        nombres_productos = self.obtener_nombres_productos()
        return nombre_producto in nombres_productos
    
    def remover_producto_por_indice(self, indice=0):
        """
        Remueve un producto del carrito según su índice.
        
        Args:
            indice (int): Índice del producto a remover (por defecto el primero)
            
        Returns:
            CartPage: Instancia actual para method chaining
            
        Raises:
            IndexError: Si el índice está fuera del rango de productos en el carrito
        """
        botones_remover = self.driver.find_elements(*self._REMOVE_BUTTONS)
        
        if indice >= len(botones_remover):
            raise IndexError(f"Índice {indice} fuera de rango. Hay {len(botones_remover)} productos en el carrito.")
        
        botones_remover[indice].click()
        return self
    
    def continuar_comprando(self):
        """
        Hace clic en el botón "Continue Shopping" para volver al inventario.
        
        Returns:
            InventoryPage: Instancia de la página de inventario
        """
        self.driver.find_element(*self._CONTINUE_SHOPPING_BUTTON).click()
        # Importación lazy para evitar dependencias circulares
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def proceder_al_checkout(self):
        """
        Hace clic en el botón "Checkout" para proceder al proceso de compra.
        
        Returns:
            CartPage: Instancia actual (o CheckoutPage cuando se implemente)
        """
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()
        # Aquí se podría retornar CheckoutPage cuando se implemente
        return self
    
    def esta_en_pagina_carrito(self):
        """
        Verifica si el usuario está actualmente en la página del carrito.
        
        Returns:
            bool: True si está en la página del carrito, False en caso contrario
        """
        return "cart.html" in self.driver.current_url