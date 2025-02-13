import sys
import csv


def parse_files():
    no_of_files = len(sys.argv)
    if no_of_files < 2 or no_of_files > 3:
        raise ValueError(
            "Please enter files in format: main.py current_year.csv [previous_year.csv]")
    return sys.argv[1:]


def read_file(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        return data


def write_file(output_file_name, data):
    with open(output_file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)
