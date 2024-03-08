import csv
from model.entity import Header
import re
from pathlib import Path


class CSVReader:
    def __init__(self, file_path):
        self.__name = None
        self.file_path = Path(file_path)
        self.delimiter = self.delimiter_sniffer() or ';'

    def __iter__(self):
        with open(self.file_path, 'r', encoding='cp1252', errors='ignore') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            next(csv_reader)

            for row in csv_reader:
                yield row

    def __str__(self):
        return f"CSV met volgende headers = {self.get_header_names()}"

    def get_name(self):
        if self.__name is None:
            name = self.file_path.stem
            self.set_name(name)

        return self.__name

    def set_name(self, name: str):
        sanitized_name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        sanitized_name = re.sub(r'^\d+', '', sanitized_name)
        if sanitized_name:
            self.__name = sanitized_name.lower()

        else:
            raise ValueError("Name cannot be empty after sanitization")

    def delimiter_sniffer(self):
        delimiters = [',', ';', '\t']  # common delimiters to check

        with open(self.file_path, 'r', encoding='cp1252', newline='') as csvfile:
            # Read the first few lines to detect the delimiter
            for line in csvfile:
                for delimiter in delimiters:
                    if delimiter in line:
                        return delimiter

        # If none of the common delimiters are found, return None
        return None

    def get_header_info(self) -> [Header]:
        with open(self.file_path, 'r', encoding='cp1252') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            csv_headers = next(csv_reader)
            csv_header_info = []
            for i, csv_header in enumerate(csv_headers):

                datatype = 'TEXT'  # alles is tekst voor het gemak van de eerste iteratie

                header = Header(csv_header, datatype)
                csv_header_info.append(header)

            return csv_header_info

    def get_header_names(self) -> [Header]:
        with open(self.file_path, 'r', encoding='cp1252') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter)
            csv_headers = next(csv_reader)
            return csv_headers
