from typing import Dict, List
import pandas as pd

def find_unused_columns(cookbook_dict: Dict[str, str], df: pd.DataFrame) -> None:
    """
    Identifies and prints the keys from the cookbook_dict that do not match any column names in the DataFrame.

    Parameters:
    - cookbook_dict: A dictionary to compare keys from.
    - df: A DataFrame to compare column names against.

    The function prints each non-matching key. If all keys match, it prints 'all checked'.
    """

    assert isinstance(cookbook_dict, dict), "cookbook_dict must be a dictionary."
    assert isinstance(df, pd.DataFrame), "df must be a pandas DataFrame."

    not_used_columns = [f"{column} not used" for column in cookbook_dict if column not in df.columns]

    if not_used_columns:
        for column_msg in not_used_columns:
            print(column_msg)
    else:
        print('all checked')