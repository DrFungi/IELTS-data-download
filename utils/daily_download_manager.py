import os
import time
import shutil
from datetime import datetime
import utils.env as credentials

class FileHandler:


    def __init__(self):
        ##### Paths to the folders
        self.download_folder = credentials.ORIGINAL_FOLDER
        self.destination_folders = [
            credentials.DOC_CENTRE,
            credentials.SEDNA
        ]

    ##### wait for the latest file to appear in the folder
    def wait_for_file(self, prefix="IELTS-download-", timeout=20):
        start_time = time.time()

        while time.time() - start_time < timeout:
            files = []
            for f in os.listdir(self.download_folder):
                if f.startswith(prefix) and f.endswith(".csv"):
                    full_path = os.path.join(self.download_folder, f)
                    files.append(full_path)

            if files:
                latest_file = max(files, key=os.path.getctime) ### preguntar si aqui hay que poner parentesis
                return latest_file
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

            ##### Rename and move the file
            new_file_path = os.path.join(self.download_folder, new_file_name)
            shutil.move(latest_file, new_file_path)

            ##### Copy to destination folders
            for dest_folder in self.destination_folders:
                dest_path = os.path.join(dest_folder, new_file_name)
                shutil.copy(new_file_path, dest_path)
                print(f"file {new_file_name}, copied to {dest_path}")

            ##### Optional Remove file
            #shutil.move(latest_file, new_file_name)
            #os.remove(original_path)
            #print(f"Original file {latest_file}. renamed as {new_file_name}")
