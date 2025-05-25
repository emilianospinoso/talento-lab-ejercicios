"""
Page Object para la página de inventario de productos de SauceDemo.
Encapsula todos los elementos y acciones relacionadas con el catálogo de productos.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Representa la página de inventario/catálogo de productos de SauceDemo.
    Proporciona métodos para interactuar con productos y navegación.
    """
    
    # Localizadores de elementos
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver):
        """
        Inicializa la página de inventario con el driver proporcionado.
        
        Args:
            driver: Instancia del WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def obtener_titulo_pagina(self):
        """
        Obtiene el título de la página de inventario.
        
        Returns:
            str: Título de la página
        """
        return self.driver.find_element(*self._TITLE).text
    
    def obtener_titulo_navegador(self):
        """
        Obtiene el título del navegador.
        
        Returns:
            str: Título del navegador
        """
        return self.driver.title
    
    def obtener_productos(self):
        """
        Obtiene la lista de elementos de productos en la página.
        
        Returns:
            list: Lista de elementos WebElement que representan productos
        """
        return self.driver.find_elements(*self._PRODUCTS)
    
    def obtener_nombres_productos(self):
        """
        Obtiene los nombres de todos los productos visibles.
        
        Returns:
            list: Lista con los nombres de los productos
        """
        elementos_nombres = self.driver.find_elements(*self._PRODUCT_NAMES)
        return [elemento.text for elemento in elementos_nombres]
    
    def obtener_cantidad_productos(self):
        """
        Obtiene la cantidad total de productos visibles.
        
        Returns:
            int: Número de productos en la página
        """
        return len(self.obtener_productos())
    
    def agregar_producto_por_indice(self, indice=0):
        """
        Añade un producto específico al carrito según su índice.
        
        Args:
            indice (int): Índice del producto a añadir (por defecto el primero)
            
        Returns:
            str: Nombre del producto añadido
            
        Raises:
            IndexError: Si el índice está fuera del rango de productos disponibles
        """
        botones_agregar = self.driver.find_elements(*self._ADD_TO_CART_BUTTONS)
        
        if indice >= len(botones_agregar):
            raise IndexError(f"Índice {indice} fuera de rango. Hay {len(botones_agregar)} productos disponibles.")
        
        # Obtener el nombre del producto antes de agregarlo
        nombres_productos = self.obtener_nombres_productos()
        nombre_producto = nombres_productos[indice]
        
        # Hacer clic en el botón correspondiente
        botones_agregar[indice].click()
        
        return nombre_producto
    
    def agregar_primer_producto(self):
        """
        Método de conveniencia para agregar el primer producto disponible.
        
        Returns:
            str: Nombre del producto añadido
        """
        return self.agregar_producto_por_indice(0)
    
    def obtener_contador_carrito(self):
        """
        Obtiene el número de productos en el carrito según el badge.
        
        Returns:
            int: Número de productos en el carrito, 0 si no hay badge visible
        """
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            # Si no hay badge visible, el carrito está vacío
            return 0
    
    def esta_carrito_vacio(self):
        """
        Verifica si el carrito está vacío (no hay badge visible).
        
        Returns:
            bool: True si el carrito está vacío, False en caso contrario
        """
        return self.obtener_contador_carrito() == 0
    
    def ir_al_carrito(self):
        """
        Navega a la página del carrito de compras.
        
        Returns:
            CartPage: Instancia de la página del carrito
        """
        self.driver.find_element(*self._CART_LINK).click()
        # Importación lazy para evitar dependencias circulares
        from pages.cart_page import CartPage
        return CartPage(self.driver)
    
    def esta_dropdown_filtro_presente(self):
        """
        Verifica si el dropdown de filtros está presente.
        
        Returns:
            bool: True si el dropdown está presente, False en caso contrario
        """
        try:
            self.driver.find_element(*self._SORT_DROPDOWN)
            return True
        except:
            return False
    
    def esta_menu_presente(self):
        """
        Verifica si el menú hamburguesa está presente.
        
        Returns:
            bool: True si el menú está presente, False en caso contrario
        """
        try:
            self.driver.find_element(*self._MENU_BUTTON)
            return True
        except:
            return False
    
    def esta_icono_carrito_presente(self):
        """
        Verifica si el ícono del carrito está presente.
        
        Returns:
            bool: True si el ícono está presente, False en caso contrario
        """
        try:
            self.driver.find_element(*self._CART_LINK)
            return True
        except:
            return False
    
    def realizar_logout(self):
        """
        Realiza el cierre de sesión del usuario.
        
        Returns:
            LoginPage: Instancia de la página de login
        """
        # Abrir el menú
        self.driver.find_element(*self._MENU_BUTTON).click()
        
        # Esperar a que el link de logout sea clickeable y hacer clic
        logout_link = self.wait.until(
            EC.element_to_be_clickable(self._LOGOUT_LINK)
        )
        logout_link.click()
        
        # Retornar instancia de LoginPage
        from pages.login_page import LoginPage
        return LoginPage(self.driver)
    
    def esta_en_pagina_inventario(self):
        """
        Verifica si el usuario está actualmente en la página de inventario.
        
        Returns:
            bool: True si está en la página de inventario, False en caso contrario
        """
        return "inventory.html" in self.driver.current_url