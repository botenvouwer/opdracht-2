import os
import requests


class Download:
    def __init__(self, urls, directory):
        self.directory = directory
        self.urls = urls
        os.makedirs(self.directory, exist_ok=True)

    def download_files(self):
        files = []

        for file_name in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file_name)
            os.remove(file_path)
            print(f"Deleted {file_name}")

        for url in self.urls:
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
                print(f"Successfully downloaded {filename}.")
                files.append(file_path)
            else:
                raise Exception(f"Kan bestand {filename} niet downloaden {response.status_code} {response.content}")

        print("All files downloaded.")
        return files
