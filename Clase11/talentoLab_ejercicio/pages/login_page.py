from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # URL de la página de login
    URL = "https://www.saucedemo.com/"
    
    # Locators (selectores de elementos)
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def abrir(self):
        """Navegar a la página de login"""
        self.driver.get(self.URL)
        return self
    
    def completar_usuario(self, usuario):
        """Escribir el nombre de usuario"""
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self
    
    def completar_clave(self, clave):
        """Escribir la contraseña"""
        campo = self.driver.find_element(*self._PASS_INPUT)
        campo.clear()
        campo.send_keys(clave)
        return self
    
    def hacer_clic_login(self):
        """Hacer clic en el botón de login"""
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self
    
    def enviar(self):
        """Alias para hacer_clic_login (compatibilidad)"""
        return self.hacer_clic_login()
    
    def login_completo(self, usuario, clave):
        """Método de conveniencia para hacer login completo"""
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_clic_login()
        return self
    
    def esta_error_visible(self):
        """Verificar si hay un mensaje de error visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False
    
    def hay_error(self):
        """Alias para esta_error_visible (compatibilidad)"""
        return self.esta_error_visible()
    
    def obtener_mensaje_error(self):
        """Obtener el texto del mensaje de error"""
        if self.esta_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""