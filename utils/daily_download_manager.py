import os
import time
import shutil
from datetime import datetime
import utils.env as credentials

class FileHandler:


    def __init__(self):
        ##### Paths to the folders
        self.download_folder = credentials.ORIGINAL_FOLDER #r"C:\Users\dville\Downloads"
        self.destination_folders = [
            r"C:\Users\dville\Documents",
            r"C:\Users\dville\Documents\Tests",
            credentials.DOC_CENTRE,
            credentials.SEDNA
        ]

    ##### wait for the file to appear in the folder
    def wait_for_file(self, prefix="IELTS-download-"):
        for _ in range(30):
            file = sorted([f for f in os.listdir(self.download_folder) if f.startswith(prefix)], reverse=True)
            if file:
                return file[0] # returns the most recent file
            time.sleep(1)
        return None

    ##### Find the latest file
    def handle_file(self):
        latest_file = self.wait_for_file()

        if not latest_file:
            print("No IELTS file found today")
        else:
            print(f"Found file: {latest_file}")

            #### get the file extension
            file_name, file_extension = os.path.splitext(latest_file)

            #### generate string to append to file
            today_string = datetime.today().strftime("%Y%m%d")
            new_file_name = f"IELTS_{today_string}{file_extension}"

            #### Full path of original nama
            original_path = os.path.join(self.download_folder, latest_file)

            #### Move and rename the file for both destinations
            for dest_folder in self.destination_folders:
                new_path = os.path.join(dest_folder,new_file_name)
                shutil.copy(original_path, new_path)
                print(f"File copied to: {new_path}")

            ##### Optional Remove file
            #os.remove(original_path)
            #print("Original file deleted.")
