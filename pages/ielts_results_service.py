
from selenium.webdriver.common.by import By
from  pages.base_page import BasePage
import utils.env as credentials
import time

from utils.daily_download_manager import FileHandler


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
    TEMPLATE_SCROLLBAR = (By.ID, "templateId")
    TEXT_OF_DOWNLOAD_TEMPLATE = "Legacy IELTS Download Template"
    FINAL_DOWNLOAD_HYPERLINK = (By.CLASS_NAME, "dialog-button-download")

    #### METHODS ####
    def __init__(self, driver):
        super().__init__(driver)

    def insert_email(self):
        self.insert_text(*self.EMAIL_TEXTBOX, self.EMAIL)

    def insert_password(self):
        self.insert_text(*self.PASSWORD_TEXTBOX, self.PASSWORD)

    def click_on_login_button(self):
        self.click_element(*self.LOGIN_BUTTON)

    def click_on_download_results(self):
        time.sleep(5)
        self.click_element(*self.DOWNLOAD_RESULTS_LINK)
        time.sleep(5)

    def is_element_present(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0

    def try_click_results_button(self, results_button):
        if self.is_element_present(results_button):  ##### this function returns true if the element is found ####
            self.click_element(*results_button)
            self.select_template(*self.TEMPLATE_SCROLLBAR, self.TEXT_OF_DOWNLOAD_TEMPLATE)
            self.click_element(*self.FINAL_DOWNLOAD_HYPERLINK)
            file_handler = FileHandler()
            file_handler.handle_file()
            print("Clicked on new results button")
        else:
            print("No new results available for download")

    def try_click_updated_results_button(self):
        if self.is_element_present(self.UPDATED_RESULTS_BUTTON):  ##### this function returns true if the element is found ####
            self.click_element(*self.UPDATED_RESULTS_BUTTON)
            self.select_template(*self.TEMPLATE_SCROLLBAR, self.TEXT_OF_DOWNLOAD_TEMPLATE)
            self.click_element(*self.FINAL_DOWNLOAD_HYPERLINK)
            self.handle_downloaded_file()
            print("Clicked on updated results button")
        else:
            print("No updated results available for download")

    ##### This function selects the specific template to download by sending umpacking the tupple TEMPLATESCROLLBAR
    ##### and effectively sending 3 arguments to select_template
    def select_IELTS_template(self):
        self.select_template(*self.TEMPLATE_SCROLLBAR, self.TEXT_OF_DOWNLOAD_TEMPLATE)

    def click_final_download_hyperlink(self):
        self.click_element(*self.FINAL_DOWNLOAD_HYPERLINK)

    ##### this method is static because it does not use any of the current class attributes
    @staticmethod
    def handle_downloaded_file():
        file_handler = FileHandler()
        file_handler.handle_file()





