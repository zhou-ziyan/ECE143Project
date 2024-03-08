from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler

def inverse_normalize_columns(df: DataFrame, column_names: list) -> DataFrame:
    """
    Applies inverse Min-Max normalization to specified columns of a pandas DataFrame.

    Parameters:
    - df (DataFrame): The DataFrame to be processed.
    - column_names (list): A list of column names to apply the inverse normalization.

    Returns:
    - DataFrame: The DataFrame with specified columns inverse normalized.
    """
    assert isinstance(df, DataFrame), "df must be a pandas DataFrame"
    assert isinstance(column_names, list), "column_names must be a list"
    
    for column_name in column_names:
        assert column_name in df.columns, f"{column_name} must be a column in the DataFrame"
        
        scaler = MinMaxScaler()
        
        normalized_data = scaler.fit_transform(df[[column_name]])
        
        df[column_name] = 1 - normalized_data
        
    return df
