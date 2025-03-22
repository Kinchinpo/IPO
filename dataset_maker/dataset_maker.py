# Standard library imports
from typing import Dict

# Third-party scientific and data processing libraries
import numpy as np
import pandas as pd

# Machine learning libraries
from sklearn.model_selection import KFold, LeaveOneOut

from config.config import CONFIG

def create_kfold_splits(
    input_data: np.ndarray,
    target: np.ndarray,
    n_splits: int = CONFIG['NUM_FOLDS'],
    random_state: int = CONFIG['RANDOM_SEED'],
    shuffle: bool = CONFIG['SHUFFLE_DATA'],
    print_info: bool = True,
) -> Dict[int, Dict[str, np.ndarray]]:
    """
    Create K-Fold cross-validation splits for the input data and target.

    Args:
        input_data (np.ndarray): The input features.
        target (np.ndarray): The target variable.
        n_splits (int, optional): Number of splits. Defaults to 5.
        random_state (int, optional): Random state for reproducibility. Defaults to 42.

    Returns:
        Dict[int, Dict[str, np.ndarray]]: A dictionary containing the train and test indices for each fold.
    """
    # Initialize KFold object
    kf: KFold = KFold(n_splits=n_splits, random_state=random_state, shuffle=shuffle)

    # Create a dictionary to store fold information
    folds: Dict[int, Dict[str, np.ndarray]] = {}

    # Generate and store splits
    for fold_index, (train_index, test_index) in enumerate(kf.split(input_data)):
        folds[fold_index] = {
            "train_index": train_index,
            "test_index": test_index
        }
        if print_info:
          # Print fold information
          print(f"Fold {fold_index}:")
          print(f"  Train: index={train_index}")
          print(f"  Test:  index={test_index}")

    return folds, kf

# Example usage
# input_data: np.ndarray = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# chemical_decom: np.ndarray = np.array([0, 1, 0, 1])

# result: Dict[int, Dict[str, np.ndarray]] = create_kfold_splits(input_data, chemical_decom)

def robust_kfold_split(X, y, n_splits=4, n_repeats=10):
    """
    Perform robust KFold split using multiple random states.

    Args:
    X (array-like): The input samples.
    y (array-like): The target values.
    n_splits (int): Number of splits for KFold.
    n_repeats (int): Number of times to repeat the KFold with different random states.

    Returns:
    list: A list of (train_index, test_index) tuples.
    """
    all_splits = []

    for i in range(n_repeats):
        random_state = np.random.randint(1, 1000)  # Generate a random state
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=random_state)
        all_splits.extend(kf.split(X, y))

    return all_splits

# Usage
# X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# y = np.array([1, 2, 3, 4])

# splits = robust_kfold_split(X, y)
# for i, (train_index, test_index) in enumerate(splits):
#     print(f"Split {i + 1}:")
#     print(f"  Train: {train_index}")
#     print(f"  Test:  {test_index}")