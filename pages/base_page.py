"""
Base Page - Clase base para todas las páginas
Contiene métodos comunes que todas las páginas heredarán
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Clase base que contiene métodos comunes para todas las páginas"""
    
    def __init__(self, driver):
        """
        Constructor de la clase BasePage
        
        Args:
            driver: Instancia del WebDriver de Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """
        Encuentra un elemento en la página
        
        Args:
            locator: Tupla con el tipo de localizador y el valor
        
        Returns:
            WebElement encontrado
        """
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """
        Hace click en un elemento
        
        Args:
            locator: Tupla con el tipo de localizador y el valor
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def enter_text(self, locator, text):
        """
        Ingresa texto en un campo
        
        Args:
            locator: Tupla con el tipo de localizador y el valor
            text: Texto a ingresar
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """
        Obtiene el texto de un elemento
        
        Args:
            locator: Tupla con el tipo de localizador y el valor
        
        Returns:
            Texto del elemento
        """
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        """
        Verifica si un elemento es visible
        
        Args:
            locator: Tupla con el tipo de localizador y el valor
        
        Returns:
            True si el elemento es visible, False en caso contrario
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """
        Obtiene la URL actual
        
        Returns:
            URL actual del navegador
        """
        return self.driver.current_url
