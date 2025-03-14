from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from drivers.driver_manager import Browser
from pages.ielts_home import IeltsHome
from pages.ielts_results_service import IeltsResultsService
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
print(driver.title)
ielts_results.insert_email()
ielts_results.insert_password()
ielts_results.click_on_login_button()
print(driver.current_url)
print(driver.title)

##### Entering the Download page for the second time #####
ielts_results.click_on_download_results()
print(driver.current_url)
print(driver.title)

##### Espacio de test para bajar el archivo #####
ielts_results.try_click_new_results_button()

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID, "templateId")))
dropdown = Select(driver.find_element(By.ID, "templateId"))
dropdown.select_by_visible_text("Legacy IELTS Download Template")

### Download the file
download_button = driver.find_element(By.CLASS_NAME, "dialog-button-download")
download_button.click()


##### Clicking in one of the download buttons
#scheduler = DownloadScheduler(ielts_results)
#scheduler.download_results_button()

###### From here will be used for development and should be deleted at the end of the project #######
'''
download_new_results = driver.find_elements(By.XPATH, "//div[@class='newresult']//a[contains(@data-action, 'downloadNewCandidates')]")
if download_new_results:
    print("element present")
else:
    print("element absent")
download_updated_results = driver.find_elements(By.XPATH, "//div[@class='updatedresult']//a[contains(@data-action, 'downloadUpdatedCandidates')]")
if download_updated_results:
    print("element present")
else:
    print("element absent")
##### printing the title's page to name the files
#second_page =ielts_home.get_title()
#titulo = driver.title
#print(original_tab)
#print(home_title)
#print(results_title)
input("press enter...")
#driver.quit()
'''