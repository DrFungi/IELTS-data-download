from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    ##### Parent class for all other pages #####
    ##### Constructor #####

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, by, value):
        self.wait.until(EC.presence_of_element_located((by, value))) ##### Ojo esta es la linea que adicione
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

    def insert_text(self, by,locator, text):
        element = self.wait.until(EC.element_to_be_clickable((by,locator)))
        element.clear()
        element.send_keys(text)

    def select_template(self, by, template_locator, template_text):
        self.wait.until(EC.visibility_of_element_located((by, template_locator)))
        dropdown = Select(self.driver.find_element(by, template_locator))
        dropdown.select_by_visible_text(template_text)

    def get_title(self):
        return self.driver.title
