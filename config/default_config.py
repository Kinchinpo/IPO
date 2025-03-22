# Standard library imports
from typing import Any, Dict, List

# Cross-validation settings
NUM_FOLDS: int = 5  # Number of folds for cross-validation
SHUFFLE_DATA: bool = True  # Whether to shuffle the data before splitting
RANDOM_SEED: int = 42  # Seed for reproducibility

# Target variable
CHEMICAL_SUBSTANCES: List[int] = [5]  # List to store chemical substances (target variables)

# MuSWEA (Multiscale Sliding Window Elimination Algorithm) parameters
WINDOW_SIZE_START: int = 6  # Starting of the sliding window size value range
WINDOW_SIZE_END: int = 12 # Ending of the sliding window size value range
WINDOW_SIZE_STEP: int = 2  # Step of the sliding window size value range
ALPHA_THRESHOLD: float = 0.05  # Significance threshold for feature selection

# Partial Least Squares (PLS) regression parameters
PLS_COMPONENTS: int = 10  # Number of components for PLS regression

# Define configuration with default values
DEFAULT_CONFIG: Dict[str, Any] = {
    # Cross-validation settings
    "NUM_FOLDS": NUM_FOLDS,
    "SHUFFLE_DATA": SHUFFLE_DATA,
    "RANDOM_SEED": RANDOM_SEED,

    # Target variable
    "CHEMICAL_SUBSTANCES": CHEMICAL_SUBSTANCES,

    # MuSWEA (Multiscale Sliding Window Elimination Algorithm) parameters
    "WINDOW_SIZE_START": WINDOW_SIZE_START,
    "WINDOW_SIZE_END": WINDOW_SIZE_END,
    "WINDOW_SIZE_STEP": WINDOW_SIZE_STEP,
    "ALPHA_THRESHOLD": ALPHA_THRESHOLD,

    # Partial Least Squares (PLS) regression parameters
    "PLS_COMPONENTS": PLS_COMPONENTS
}