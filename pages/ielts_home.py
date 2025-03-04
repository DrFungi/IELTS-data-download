
from selenium.webdriver.common.by import By
from  pages.base_page import BasePage


class IeltsHome(BasePage):
    IELTS_HOME_URL = "https://ielts.org/organisations/ielts-for-organisations/verifying-ielts-results#login"
    ACCEPT_COOKIES = (By.ID, "onetrust-accept-btn-handler")
    LOGIN_LINK = (By.LINK_TEXT, "Log in to your IELTS Results Service account")

    def __init__(self, driver):
        super().__init__(driver)

    def open_ielts_home(self):
        self.open_page(self.IELTS_HOME_URL)

    def accept_cookies(self):
        self.click_element(*self.ACCEPT_COOKIES)

    def click_on_login_link(self):
        self.driver.maximize_window() # use this when working in the small screen
        self.click_element(*self.LOGIN_LINK)

