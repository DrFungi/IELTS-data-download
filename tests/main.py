from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers.driver_manager import Browser
from pages.ielts_home import IeltsHome
from pages.ielts_results_service import IeltsResultsService
from utils.daily_download_manager import FileHandler
from utils.download_scheduler import DownloadScheduler

#import os


##### Initialize the browser #####
browser = Browser(headless=False) #constructor options for headless or browser come here. ex. headless=True
driver = browser.get_driver()

##### Entering the IELTS portal #####
ielts_home = IeltsHome(driver)
ielts_home.open_ielts_home()
home_title = ielts_home.get_title()

##### Accepting cookies #####
ielts_home.accept_cookies()
assert len(driver.window_handles) == 1

##### Entering the downloads page #####
ielts_home.click_on_login_link()
ielts_home.wait_second_tab()
ielts_home.switch_to_new_tab()

##### Entering credentials #####
ielts_results = IeltsResultsService(driver)
#print(driver.title)
ielts_results.insert_email()
ielts_results.insert_password()
ielts_results.click_on_login_button()
#print(driver.current_url)
#print(driver.title)

##### Entering the Download page for the second time #####
ielts_results.click_on_download_results()
#print(driver.current_url)
#print(driver.title)


##### Clicking in one of the download buttons and downloading the file
scheduler = DownloadScheduler(ielts_results)
scheduler.download_results_button()

##### Selecting and downloading the file
#ielts_results.select_IELTS_template()
#ielts_results.click_final_download_hyperlink()

##### Handle the downloaded file
#file_handler = FileHandler()
#file_handler.handle_file()

##### Espacio de test para bajar el archivo #####
#ielts_results.try_click_new_results_button()

##### Download the file
#download_button = driver.find_element(By.CLASS_NAME, "dialog-button-download")
#download_button.click()
