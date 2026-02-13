from selenium.webdriver.common.by import By
from Script.modules.utils.loginUtils import BasePage


class CheckoutPage(BasePage):
    
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def fill_form(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click_element(self.FINISH_BUTTON)

    def get_complete_header(self):
        return self.get_text(self.COMPLETE_HEADER)

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)
