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
        """
        Constructor que recibe la instancia del WebDriver
        """
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
    
    def enviar(self):
        """Hacer clic en el botón de login"""
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self
    
    def login_completo(self, usuario, clave):
        """Método de conveniencia para hacer login completo"""
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.enviar()
        return self
    
    def hay_error(self):
        """Verificar si hay un mensaje de error visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except:
            return False
    
    def obtener_mensaje_error(self):
        """Obtener el texto del mensaje de error"""
        if self.hay_error():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""