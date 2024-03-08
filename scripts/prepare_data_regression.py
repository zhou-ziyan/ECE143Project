from pandas import DataFrame
from sklearn.model_selection import train_test_split
import numpy as np

def prepare_data_for_regression(df: DataFrame, target_column: str, features_not_include: list) -> tuple:
    """
    Cleans the DataFrame, selects features for regression, and splits it into features and target datasets.

    Parameters:
    - df (DataFrame): The input DataFrame to be processed.
    - target_column (str): The name of the column to be used as the target variable.
    - features_not_include (list): A list of column names to exclude from the feature set.

    Returns:
    - tuple: A tuple containing the features DataFrame `X`, the target Series `y`, the feature names list, and `df_cleaned`
    """
    # Clean the DataFrame
    df_cleaned = df[~df.isin([-99999]).any(axis=1)]
    df_cleaned.dropna(inplace=True)

    # Select features
    feature_list = [x for x in df_cleaned.columns if x not in features_not_include]

    # Split the DataFrame into features and target
    X = df_cleaned[feature_list]
    y = df_cleaned[target_column]

    return X, y, feature_list, df_cleaned


