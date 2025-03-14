
from selenium.webdriver.common.by import By
from  pages.base_page import BasePage
import utils.env as credentials
import time

class IeltsResultsService(BasePage):

    #### CREDENTIALS #####
    EMAIL = credentials.EMAIL
    PASSWORD = credentials.PASSWORD

    #### LOCATORS ####
    EMAIL_TEXTBOX = (By.NAME, "email")
    PASSWORD_TEXTBOX = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "auth0-lock-submit")
    DOWNLOAD_RESULTS_LINK = (By.LINK_TEXT, "Download Results")
    NEW_RESULTS_BUTTON = (By.XPATH, "//div[@class='newresult']//a[contains(@data-action, 'downloadNewCandidates')]")
    UPDATED_RESULTS_BUTTON = (By.XPATH, "//div[@class='updatedresult']//a[contains(@data-action, 'downloadUpdatedCandidates')]")

    #### METHODS ####
    def __init__(self, driver):
        super().__init__(driver)

    def insert_email(self):
        self.insert_text(self.EMAIL_TEXTBOX, self.EMAIL)

    def insert_password(self):
        self.insert_text(self.PASSWORD_TEXTBOX, self.PASSWORD)

    def click_on_login_button(self):
        self.click_element(*self.LOGIN_BUTTON)

    def click_on_download_results(self):
        time.sleep(5)
        self.click_element(*self.DOWNLOAD_RESULTS_LINK)
        time.sleep(5)

    def is_element_present(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0

    def try_click_new_results_button(self):
        if self.is_element_present(self.NEW_RESULTS_BUTTON):  ##### this function returns true if the element is found ####
            self.click_element(*self.NEW_RESULTS_BUTTON)
            print("Clicked on new results button")
        else:
            print("No new results available for download")

    def try_click_updated_results_button(self):
        if self.is_element_present(self.UPDATED_RESULTS_BUTTON):  ##### this function returns true if the element is found ####
            self.click_element(*self.UPDATED_RESULTS_BUTTON)
            print("Clicked on updated results button")
        else:
            print("No updated results available for download")


