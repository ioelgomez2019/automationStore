"""
Login Page - Page Object para la página de login de SauceDemo
Contiene los elementos y acciones de la página de login
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Clase que representa la página de Login de SauceDemo"""
    
    # URL de la página
    URL = "https://www.saucedemo.com/"
    
    # Localizadores de elementos de la página
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    # Localizador para verificar login exitoso
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    
    def __init__(self, driver):
        """
        Constructor de la clase LoginPage
        
        Args:
            driver: Instancia del WebDriver de Selenium
        """
        super().__init__(driver)
    
    def open(self):
        """Abre la página de login"""
        self.driver.get(self.URL)
    
    def enter_username(self, username):
        """
        Ingresa el nombre de usuario
        
        Args:
            username: Nombre de usuario a ingresar
        """
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """
        Ingresa la contraseña
        
        Args:
            password: Contraseña a ingresar
        """
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Hace click en el botón de login"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Realiza el proceso completo de login
        
        Args:
            username: Nombre de usuario
            password: Contraseña
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def is_error_message_displayed(self):
        """
        Verifica si se muestra un mensaje de error
        
        Returns:
            True si hay un mensaje de error, False en caso contrario
        """
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def get_error_message(self):
        """
        Obtiene el texto del mensaje de error
        
        Returns:
            Texto del mensaje de error
        """
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_login_successful(self):
        """
        Verifica si el login fue exitoso
        
        Returns:
            True si el login fue exitoso, False en caso contrario
        """
        return self.is_element_visible(self.PRODUCTS_TITLE)
    
    def get_products_title(self):
        """
        Obtiene el título de la página de productos
        
        Returns:
            Texto del título de productos
        """
        return self.get_text(self.PRODUCTS_TITLE)
