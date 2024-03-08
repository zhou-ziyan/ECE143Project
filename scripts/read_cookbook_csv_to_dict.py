import csv
from typing import Dict

def read_cookbook_csv_to_dict(file_path: str) -> Dict[str, str]:
    """
    Reads a CSV file and converts it into a dictionary.

    The CSV file should have at least two columns. The function uses the first column as keys
    and the second column as values for the dictionary.

    Parameters:
    - file_path: The path to the CSV file to be read.

    Returns:
    - A dictionary with keys from the first column and values from the second column of the CSV.

    Raises:
    - AssertionError: If the file_path is not a string or is empty.
    - FileNotFoundError: If the file_path does not point to an existing file.
    """

    # Assertions to ensure correctness of input data
    assert isinstance(file_path, str), "The file_path must be a string."
    assert file_path, "The file_path cannot be empty."

    cookbook_dict = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if reader.line_num == 1:  # Skip the header row
                continue
            key, value = row[0], row[1]
            cookbook_dict[key] = value

    return cookbook_dict

if __name__ == "__main__":
    base_path = 'dataset/'
    cookbook_file_path = base_path + 'cookbook.csv'
    try:
        cookbook_dict = read_cookbook_csv_to_dict(cookbook_file_path)
        print(cookbook_dict)
    except FileNotFoundError:
        print(f"The file {cookbook_file_path} does not exist.")
