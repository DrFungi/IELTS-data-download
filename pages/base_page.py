from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    ##### Parent class for all other pages #####
    ##### Constructor #####

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def get_open_tabs(self):
        tabs = self.driver.window_handles
        print(tabs)

    def wait_second_tab(self):
        self.wait.until(EC.number_of_windows_to_be(2))

    def switch_to_new_tab(self):
        original_tab = self.driver.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        # Loop through until we find a new window handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_tab:
                self.driver.switch_to.window(window_handle)
                break

    def insert_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def get_title(self):
        return self.driver.title