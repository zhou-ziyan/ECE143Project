import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sort_correlations(corr_matrix: pd.DataFrame, target_var: str) -> pd.Series:
    """Sort correlations of the target variable with others in descending order.
    
    Args:
        corr_matrix: The correlation matrix of the dataset.
        target_var: The target variable for which correlations are to be sorted.
        
    Returns:
        A Series containing sorted correlations of the target variable.
    """
    return corr_matrix[target_var].sort_values(ascending=False)

def plot_correlation_barplot(correlations: pd.Series, figsize: tuple=(20, 15), palette: str="coolwarm"):
    """Plot a barplot for the correlations of the target variable with others.
    
    Args:
        correlations: A Series containing the sorted correlations of the target variable.
        figsize: The figure size of the plot.
        palette: The color palette of the barplot.
    """
    plt.figure(figsize=figsize)
    sns.barplot(x=correlations.index, y=correlations.values, palette=palette)
    plt.title("Correlation of Walkability Index with Other Variables")
    plt.xlabel("Variables")
    plt.ylabel("Correlation Coefficient")
    plt.xticks(rotation=45)
    plt.xticks(np.arange(len(correlations.index)), correlations.index, fontsize=8, ha='right')

    # for index, variable in enumerate(walkability_corr.index):
    #     plt.text(index, walkability_corr.values[index], variable, ha='center', va='bottom', fontsize=8, rotation=45)

    plt.show()

# For corr_matrix
# walkability_corr = sort_correlations(corr_matrix, "NatWalkInd")
# plot_correlation_barplot(walkability_corr)
