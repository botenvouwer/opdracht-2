import os
import requests
from constants import directory, urls


class Download:
    def __init__(self):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def download_files(self):
        files = []
        for url in urls:
            # Extract the filename from the URL
            filename = url.split('/')[-1]

            # Specify the full path to save the file
            file_path = os.path.join(self.directory, filename)

            # Send an HTTP GET request to fetch the file content
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Write the content of the response to a local file
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {filename} successfully.")
                files.append(file_path)
            else:
                print(f"Failed to download {filename}.")

        print("All files downloaded.")
        return files
