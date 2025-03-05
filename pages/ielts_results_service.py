from selenium.webdriver.common.by import By
from  pages.base_page import BasePage
import utils.env as credentials

class IeltsResultsService(BasePage):

    #### CREDENTIALS #####
    EMAIL = credentials.EMAIL
    PASSWORD = credentials.PASSWORD

    #### LOCATORS ####
    EMAIL_TEXTBOX = (By.NAME, "email")
    PASSWORD_TEXTBOX = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "auth0-lock-submit")

    #### METHODS ####
    def __init__(self, driver):
        super().__init__(driver)

    def insert_email(self):
        self.insert_text(self.EMAIL_TEXTBOX, self.EMAIL)

    def insert_password(self):
        self.insert_text(self.PASSWORD_TEXTBOX, self.PASSWORD)

    def click_on_login_button(self):
        self.click_element(*self.LOGIN_BUTTON)