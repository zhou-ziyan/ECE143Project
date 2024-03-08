from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

def train_and_evaluate_regression_model(X: DataFrame, y: DataFrame, test_size: float = 0.2, random_state: int = 42) -> tuple:
    """
    Trains and evaluates a linear regression model.

    Parameters:
    - X (DataFrame): The features DataFrame.
    - y (DataFrame): The target variable Series.
    - test_size (float): The proportion of the dataset to include in the test split.
    - random_state (int): Controls the shuffling applied to the data before applying the split.

    Returns:
    - tuple: A tuple containing the trained model and the mean squared error (MSE) of the model's predictions.
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")

    return model, mse
