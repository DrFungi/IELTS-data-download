
from drivers.driver_manager import Browser
from pages.ielts_home import IeltsHome
from pages.ielts_results_service import IeltsResultsService

#import os


##### Initialize the browser #####
browser = Browser(headless=False) #constructor options for headless or browser come here. ex. headless=True
driver = browser.get_driver()

##### Entering the IELTS portal #####
ielts_home = IeltsHome(driver)
ielts_home.open_ielts_home()
home_title = ielts_home.get_title()
ielts_home.accept_cookies()
assert len(driver.window_handles) == 1
ielts_home.click_on_login_link()
ielts_home.wait_second_tab()
ielts_home.switch_to_new_tab()
ielts_results = IeltsResultsService(driver)
ielts_results.insert_email()
ielts_results.insert_password()
ielts_results.click_on_login_button()
results_title = ielts_results.get_title()


##### printing the title's page to name the files
#second_page =ielts_home.get_title()
#titulo = driver.title
#print(original_tab)
print(home_title)
print(results_title)


#input("press enter...")
#driver.quit()