
import datetime
from pages.ielts_results_service import IeltsResultsService

class DownloadScheduler:
    def __init__(self, results_page: IeltsResultsService):
        self.results_page = results_page

    def download_results_button(self):
        day = datetime.date.today().strftime('%A') # This gets the current day as string

        if day in ["Monday", "Wednesday"]:
            self.results_page.try_click_new_results_button()
        elif day in ["Tuesday", "Thursday"]:
            self.results_page.try_click_updated_results_button()
        else:
            print("No downloads scheduled for today.")