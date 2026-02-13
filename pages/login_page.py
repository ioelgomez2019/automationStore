from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    
    URL = "https://www.saucedemo.com/"
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        self.driver.get(self.URL)
    
    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def is_error_message_displayed(self):
        return self.is_element_visible(self.ERROR_MESSAGE)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_login_successful(self):
        return self.is_element_visible(self.PRODUCTS_TITLE)
    
    def get_products_title(self):
        return self.get_text(self.PRODUCTS_TITLE)
