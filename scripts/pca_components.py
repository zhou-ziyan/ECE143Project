from typing import Any
import numpy as np
from sklearn.decomposition import PCA

def print_pca_components_info(pca_model: PCA, columns: Any, num_components: int = 5, num_features: int = 5):
    """
    Prints the top contributing features for the first few principal components of a PCA model.
    
    :param pca_model: Fitted PCA model.
    :param columns: Column names corresponding to the features in the PCA model.
    :param num_components: Number of principal components to display.
    :param num_features: Number of top contributing features to display for each component.
    """
    assert isinstance(pca_model, PCA), "pca_model must be an instance of sklearn.decomposition.PCA"
    assert num_components > 0, "num_components must be a positive integer"
    assert num_features > 0, "num_features must be a positive integer"
    
    explained_variance_ratio = pca_model.explained_variance_ratio_
    components = pca_model.components_
    
    for i in range(min(num_components, len(components))):  # To handle cases where num_components > len(components)
        print(f"Principal Component {i+1}:")
        component_values = components[i]
        component_indices = np.argsort(np.abs(component_values))[::-1]
        for j in component_indices[:num_features]:
            print(f"\t{columns[j]}: {component_values[j]}")


def create_components_dict(components, walkability_df_numeric_data, explained_variance_ratio, num_comp):
    """
    Create a dictionary containing information about each principal component.

    Args:
        components (array-like): The components of the PCA model.
        walkability_df_numeric_data (DataFrame): The DataFrame containing numeric data.
        explained_variance_ratio (array-like): The explained variance ratio of each principal component.
        num_comp (int): The number of principal components.

    Returns:
        dict: A dictionary containing information about each principal component.
            Each key represents a principal component, and the corresponding value is a dictionary
            containing columns and their corresponding weights, as well as the variance explained by the component.
    """
    components_dict = {}

    for i in range(num_comp):
        component_info = {}
        component_values = components[i]
        component_indices = np.argsort(np.abs(component_values))[::-1]

        for j in component_indices:
            component_info[walkability_df_numeric_data.columns[j]] = component_values[j]

        components_dict[f"Principal Component {i+1}"] = {
            "Columns": component_info,
            "Variance Explained": explained_variance_ratio[i] * 100
        }

    return components_dict


def normalize_components(components_dict):
    """
    Normalize the weights of each principal component in the components_dict.

    Args:
        components_dict (dict): A dictionary containing information about each principal component.
            Each key represents a principal component, and the corresponding value is a dictionary
            containing columns and their corresponding weights.

    Returns:
        dict: A dictionary containing normalized weights for each principal component.
            Each key represents a principal component, and the corresponding value is a dictionary
            containing columns and their normalized weights, as well as the variance explained by the component.
    """
    normalized_components_dict = {}

    for i, component_key in enumerate(components_dict.keys()):
        component_info = components_dict[component_key]

        component_columns = component_info["Columns"]
        component_values = list(component_columns.values())

        # Take the absolute values of the weights
        abs_component_values = [abs(value) for value in component_values]

        # Normalize the weights so that they sum up to 1
        normalized_values = [value / sum(abs_component_values) for value in abs_component_values]

        normalized_components_dict[component_key] = {
            "Columns": {column: normalized_values[j] for j, column in enumerate(component_columns)},
            "Variance Explained": component_info["Variance Explained"]
        }

    return normalized_components_dict