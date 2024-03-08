import pandas as pd
from typing import List


def load_and_clean_happiness_data(happiness_file_path: str, columns_to_drop: list) -> pd.DataFrame:
    """
    Loads happiness data from a CSV file, removes specified columns, and returns the cleaned DataFrame.
    
    :param happiness_file_path: String, the file path of the CSV file containing happiness data.
    :param columns_to_drop: List of strings, column names to be removed from the DataFrame.
    :return: A pandas DataFrame with the specified columns dropped.
    """
    assert isinstance(happiness_file_path, str), "happiness_file_path must be a string"
    assert isinstance(columns_to_drop, list), "columns_to_drop must be a list"
    assert all(isinstance(column, str) for column in columns_to_drop), "All elements in columns_to_drop must be strings"
    
    happiness_df = pd.read_csv(happiness_file_path)
    
    # Drop specified columns
    happiness_df = happiness_df.drop(columns=columns_to_drop)

    # happiness_df.columns
    # happiness_df
    
    return happiness_df


def preprocess_dataframe(df: pd.DataFrame, na_subset: List[str], int_column: str) -> pd.DataFrame:
    """
    Cleans and processes the input dataframe by dropping specified columns, dropping rows based on NaN values in 
    a specified subset of columns, and converting a specified column to integer type.
    
    :param df: The dataframe to preprocess.
    :param na_subset: A list of column names to check for NaN values before dropping rows.
    :param int_column: The name of the column to convert to integer type.
    :return: The preprocessed dataframe.
    """
    assert isinstance(df, pd.DataFrame), "df must be a pandas DataFrame"
    assert isinstance(na_subset, list), "na_subset must be a list"
    assert isinstance(int_column, str), "int_column must be a string"
    
    # Drop rows based on NaN values in the specified subset of columns
    df = df.dropna(subset=na_subset)
    
    # Convert specified column to integer type
    df[int_column] = df[int_column].astype(int)
    
    return df


def merge_dataframes_on_cbsa(df1: pd.DataFrame, df2: pd.DataFrame, merge_column: str = 'CBSA') -> pd.DataFrame:
    """
    Merges two DataFrames based on the specified merge_column using an inner join.

    Parameters:
    - df1 (DataFrame): The first DataFrame to merge.
    - df2 (DataFrame): The second DataFrame to merge.
    - merge_column (str): The column name on which to perform the merge.

    Returns:
    - DataFrame: The resulting merged DataFrame.
    """
    assert isinstance(df1, pd.DataFrame), "df1 must be a pandas DataFrame"
    assert isinstance(df2, pd.DataFrame), "df2 must be a pandas DataFrame"
    assert isinstance(merge_column, str), "merge_column must be a string"
    assert merge_column in df1.columns, f"{merge_column} must be a column in df1"
    assert merge_column in df2.columns, f"{merge_column} must be a column in df2"

    merged_df = pd.merge(df1, df2, on=merge_column, how='inner')

    # merged_df.columns.values
    
    return merged_df

def calculate_and_merge_average_natwalkind(merged_df: pd.DataFrame) -> (pd.DataFrame, pd.DataFrame):
    """
    Calculates the average 'NatWalkInd' for each 'City' and 'CBSA' combination in the merged DataFrame,
    then merges this average back into the original DataFrame without the original 'NatWalkInd' column.
    Also ensures no duplicate rows in the final DataFrame.

    Parameters:
    - merged_df (DataFrame): The merged DataFrame containing 'City', 'CBSA', and 'NatWalkInd' columns.

    Returns:
    - Tuple[DataFrame, DataFrame]: A tuple containing:
        - The DataFrame with calculated averages ('average_df').
        - The original merged DataFrame with 'NatWalkInd' replaced by the averages and duplicates removed ('merged_with_average').
    """
    assert isinstance(merged_df, pd.DataFrame), "merged_df must be a pandas DataFrame"
    assert 'City' in merged_df.columns and 'CBSA' in merged_df.columns and 'NatWalkInd' in merged_df.columns, \
        "merged_df must contain 'City', 'CBSA', and 'NatWalkInd' columns"

    # Calculate the average 'NatWalkInd' for each 'City' and 'CBSA'
    average_df = merged_df.groupby(['City', 'CBSA'])['NatWalkInd'].mean().reset_index()
    average_df.rename(columns={'NatWalkInd': 'Average NatWalkInd'}, inplace=True)

    # Merge the average back into the original DataFrame, excluding the original 'NatWalkInd'
    merged_with_average = pd.merge(merged_df.drop(columns=['NatWalkInd']), average_df, on=['City', 'CBSA'], how='right')
    merged_with_average.drop_duplicates(inplace=True)

    return average_df, merged_with_average