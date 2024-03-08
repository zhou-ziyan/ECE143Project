import pandas as pd
from typing import Dict, List

def print_column_cookbook_descriptions(df: pd.DataFrame, description_dict: Dict[str, str]) -> None:
    """
    Prints descriptions for each column in the DataFrame based on the provided description dictionary.
    If a column's description is not found in the dictionary, it prints a default message indicating
    no description is available. Also, prints a message if all columns have been checked.

    Parameters:
    - df: A pandas DataFrame whose columns are to be checked against the description dictionary.
    - description_dict: A dictionary where keys are column names and values are their descriptions.

    Raises:
    - AssertionError: If the input types are not as expected.
    """

    assert isinstance(df, pd.DataFrame), "The first argument must be a pandas DataFrame."
    assert isinstance(description_dict, Dict), "The second argument must be a dictionary."

    no_description_columns = []

    for column in df.columns.values:
        if column in description_dict:
            print(f'{column}: {description_dict[column]}')
        else:
            no_description_columns.append(column)
            print(f'{column}: no description')  # No description available in codebook.

    if not no_description_columns:
        print('All columns have descriptions.')
    else:
        print('Columns without descriptions:', ', '.join(no_description_columns))