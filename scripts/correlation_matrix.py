import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def drop_unnecessary_columns(df: pd.DataFrame, columns_to_drop: list) -> pd.DataFrame:
    """Drop specified columns from the DataFrame.
    
    Args:
        df: The original DataFrame.
        columns_to_drop: A list of column names to be dropped.
        
    Returns:
        The DataFrame with specified columns removed.
    """
    return df.drop(columns=columns_to_drop)

def move_column_to_first(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Move a specified column to the first position.
    
    Args:
        df: The DataFrame to be rearranged.
        column_name: The name of the column to move.
        
    Returns:
        The DataFrame with the specified column moved to the first position.
    """
    columns = list(df.columns)
    columns.insert(0, columns.pop(columns.index(column_name)))
    return df.reindex(columns=columns)

def plot_correlation_matrix(df: pd.DataFrame, figsize: tuple=(10, 10), cmap: str='coolwarm') -> pd.DataFrame:
    """Plot the correlation matrix of the DataFrame.
    
    Args:
        df: The DataFrame for which the correlation matrix is computed.
        figsize: The figure size of the plot.
        cmap: The colormap of the heatmap.

    Returns:
        The DataFrame with the correlation matrix.
    """
    corr_matrix = df.corr()
    plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, annot=False, fmt=".2f", cmap=cmap)
    plt.title("Correlation Matrix of Walkability Index")
    plt.show()

    return corr_matrix

columns_to_drop = [
    "OBJECTID", "GEOID10", "GEOID20", "STATEFP", "COUNTYFP",
    "TRACTCE", "BLKGRPCE", "CSA", "CSA_Name", "CBSA", "CBSA_Name"
]

# For walkability_df
# walkability_df_numeric_data = drop_unnecessary_columns(walkability_df, columns_to_drop)
# walkability_df_numeric_data = move_column_to_first(walkability_df_numeric_data, 'NatWalkInd')
# corr_matrix = plot_correlation_matrix(walkability_df_numeric_data)
