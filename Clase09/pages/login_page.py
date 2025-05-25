"""
Page Object para la página de inicio de sesión de SauceDemo.
Encapsula todos los elementos y acciones relacionadas con el login.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Representa la página de inicio de sesión de SauceDemo.
    Proporciona métodos para interactuar con los elementos de login.
    """
    
    # URL de la página de login
    URL = "https://www.saucedemo.com/"
    
    # Localizadores de elementos (privados y centralizados)
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        """
        Inicializa la página de login con el driver proporcionado.
        
        Args:
            driver: Instancia del WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def abrir(self):
        """
        Navega a la página de login.
        
        Returns:
            LoginPage: Instancia actual para method chaining
        """
        self.driver.get(self.URL)
        return self
    
    def ingresar_usuario(self, usuario):
        """
        Ingresa el nombre de usuario en el campo correspondiente.
        
        Args:
            usuario (str): Nombre de usuario a ingresar
            
        Returns:
            LoginPage: Instancia actual para method chaining
        """
        campo_usuario = self.wait.until(
            EC.visibility_of_element_located(self._USERNAME_INPUT)
        )
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)
        return self
    
    def ingresar_password(self, password):
        """
        Ingresa la contraseña en el campo correspondiente.
        
        Args:
            password (str): Contraseña a ingresar
            
        Returns:
            LoginPage: Instancia actual para method chaining
        """
        campo_password = self.driver.find_element(*self._PASSWORD_INPUT)
        campo_password.clear()
        campo_password.send_keys(password)
        return self
    
    def hacer_clic_login(self):
        """
        Hace clic en el botón de login.
        
        Returns:
            LoginPage: Instancia actual para method chaining
        """
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self
    
    def realizar_login(self, usuario, password):
        """
        Método de conveniencia que realiza el login completo.
        
        Args:
            usuario (str): Nombre de usuario
            password (str): Contraseña
            
        Returns:
            LoginPage: Instancia actual para method chaining
        """
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_clic_login()
        return self
    
    def esta_mensaje_error_visible(self):
        """
        Verifica si hay un mensaje de error visible en la página.
        
        Returns:
            bool: True si el mensaje de error está visible, False en caso contrario
        """
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False
    
    def obtener_mensaje_error(self):
        """
        Obtiene el texto del mensaje de error.
        
        Returns:
            str: Texto del mensaje de error, cadena vacía si no hay error
        """
        if self.esta_mensaje_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""
    
    def esta_en_pagina_login(self):
        """
        Verifica si el usuario está actualmente en la página de login.
        
        Returns:
            bool: True si está en la página de login, False en caso contrario
        """
        return self.driver.current_url == self.URL