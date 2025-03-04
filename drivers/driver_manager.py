
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self, headless=False, browser="chrome"):
        if browser == "chrome":
            # Create an options object to customize browser settings
            options = Options()
            #options.add_argument("--incognito")
            options.add_experimental_option("detach", True)

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("disable-gpu") # recommended for headless mode - avoids using GPU acceleration

            # Create a service object that verifies and downloads if needed the
            # correct version of chromedriver.exe
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError("Unsupported browser")

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()




"""
I will include here a version on how to manage the chromedriver.exe manually
in case the automatic one ever breaks
I am also leaving the current (as of 2025-02-23) version of the chromedriver.exe

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = r"chromedriver-win64/chromedriver.exe"


class Browser:

    def __init__(self, headless=False):

        # Create a Service object with the WebDriver path
        service = Service(executable_path=DRIVER_PATH)

        # Create an Options object to customize browser settings (optional)
        options = Options()
        options.add_argument("--incognito")  # Use Incognito mode (Chrome equivalent of --inprivate)
        options.add_experimental_option("detach", True) #keeps browser open

        # Initialize the Chrome WebDriver with the service and options
        if headless:
            options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self):
        return self.driver

    def close(self):
        self.driver.quit()

"""