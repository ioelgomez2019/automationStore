from selenium.webdriver.common.by import By
from Script.modules.utils.loginUtils import BasePage


class CartPage(BasePage):
    
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)
