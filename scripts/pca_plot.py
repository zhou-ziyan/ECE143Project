from typing import Tuple, List
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


def normalize_data(data: pd.DataFrame) -> np.ndarray:
    """
    Normalize the input numerical data using max normalization.

    Args:
    - data (pd.DataFrame): The numerical data to be normalized.

    Returns:
    - np.ndarray: The normalized numerical data as a Numpy array.
    """
    assert isinstance(data, pd.DataFrame), "Input data must be a pandas DataFrame."
    
    normalized_data = normalize(data.dropna().values, axis=0, norm='max')
    return normalized_data

def perform_pca(data: np.ndarray, n_components: int = 20) -> PCA:
    """
    Perform Principal Component Analysis (PCA) on the normalized data.

    Args:
    - data (np.ndarray): The normalized data on which PCA should be performed.
    - n_components (int): The number of principal components to consider.

    Returns:
    - PCA: The PCA model after fitting the data.
    """
    assert isinstance(data, np.ndarray), "Input data must be a numpy array."
    assert isinstance(n_components, int) and n_components > 0, "Number of components must be a positive integer."
    
    pca = PCA(n_components=n_components)
    pca.fit(data)
    return pca

def plot_scree(pca: PCA, figsize: Tuple[int, int] = (8, 6)) -> None:
    """
    Plot the Scree plot of the explained variance by each principal component.

    Args:
    - pca (PCA): The PCA model containing explained variance information.
    - figsize (Tuple[int, int]): The figure size for the plot.
    """
    assert isinstance(pca, PCA), "Input must be a PCA model."
    assert len(figsize) == 2 and all(isinstance(i, int) for i in figsize), "Figsize must be a tuple of two integers."

    plt.figure(figsize=figsize)
    num_comp = len(pca.explained_variance_)
    plt.plot(np.arange(1, num_comp + 1), pca.explained_variance_, marker='o', linestyle='-')
    plt.xlabel('Principal Component Number', fontsize=12)
    plt.ylabel('Explained Variance', fontsize=12)
    plt.title('Scree Plot', fontsize=14)
    plt.grid(True)
    plt.show()

def plot_stacked_bar(normalized_components_dict):
    """
    Plot a stacked bar chart showing the weights of each column for each principal component.

    Args:
        normalized_components_dict (dict): A dictionary containing normalized weights for each principal component.

    Returns:
        None
    """
    component_keys = list(normalized_components_dict.keys())
    columns = list(normalized_components_dict[component_keys[0]]["Columns"].keys())

    fig, ax = plt.subplots(figsize=(20, 15))

    for i, component_key in enumerate(component_keys):
        normalized_values = list(normalized_components_dict[component_key]["Columns"].values())
        # print(sum(normalized_values)) # 1

        if i == 0:
            ax.bar(columns, normalized_values, label=component_key)
        else:
            bottom_values = [sum(values) for values in zip(*[list(normalized_components_dict[key]["Columns"].values()) for key in component_keys[:i]])]
            ax.bar(columns, normalized_values, bottom=bottom_values, label=component_key)

    ax.set_xlabel('Features', fontsize=12)
    ax.set_ylabel('Normalized Weight', fontsize=12)
    ax.set_title('Stacked Bar Chart of Principal Components', fontsize=14)
    ax.legend(loc='upper right', fontsize=10)

    plt.xticks(rotation=45)
    plt.xticks(fontsize=8, ha='right')

    plt.show()

def pca_plot_scatter(numerical_matrix_normalized):
    """
    Perform PCA on normalized numerical data and plot a scatter plot of the top 2 principal components using Seaborn.

    Args:
        numerical_matrix_normalized (array-like): The normalized numerical data matrix.
        num_comp_selected (int): The number of principal components to retain.

    Returns:
        None
    """
    pca_selected = PCA(n_components=2)
    pca_selected.fit(numerical_matrix_normalized)

    transformed_data = pca_selected.transform(numerical_matrix_normalized)

    df_transformed = pd.DataFrame(transformed_data, columns=[f"Principal Component {i+1}" for i in range(2)])

    sns.scatterplot(data=df_transformed, x='Principal Component 1', y='Principal Component 2', alpha=0.3, edgecolor=None)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Matching 5000 Data Points Sample to the Top 2 PCA Components')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()