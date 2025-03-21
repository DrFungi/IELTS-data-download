
import datetime
from pages.ielts_results_service import IeltsResultsService
#from tests.main import ielts_results


class DownloadScheduler:
    def __init__(self, ielts_results: IeltsResultsService):
        self.ielts_results = ielts_results

    def download_results_button(self):
        day = datetime.date.today().strftime('%A') # This gets the current day as string

        if day in ["Monday", "Wednesday"]:
            self.ielts_results.try_click_results_button(self.ielts_results.NEW_RESULTS_BUTTON, results="new")
        elif day in ["Tuesday", "Thursday"]:
            self.ielts_results.try_click_results_button(self.ielts_results.UPDATED_RESULTS_BUTTON, results="updated")
            #self.ielts_results.try_click_updated_results_button()
        else:
            print("No downloads scheduled for today.")