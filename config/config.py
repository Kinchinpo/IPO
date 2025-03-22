"""Configuration for data processing and analysis using MuSWEA and regression models."""

# Standard library imports
from typing import Any, Dict, List

from config.default_config import DEFAULT_CONFIG

def validate_and_set_defaults(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate the configuration and set default values if needed.

    Args:
        config (Dict[str, Any]): The configuration dictionary.

    Returns:
        Dict[str, Any]: The validated and updated configuration dictionary.

    Raises:
        ValueError: If any of the configuration values are invalid.
    """
    defaults = {
        "NUM_FOLDS": 5,
        "SHUFFLE_DATA": True,
        "RANDOM_SEED": 42,
        "WINDOW_SIZE_START": 6,
        "WINDOW_SIZE_END": 12,
        "WINDOW_SIZE_STEP": 2,
        "ALPHA_THRESHOLD": 0.05,
        "PLS_COMPONENTS": 10
    }

    for key, default_value in defaults.items():
        if key not in config:
            config[key] = default_value

        # Type checking and value validation
        if key in ["NUM_FOLDS", "RANDOM_SEED", "WINDOW_SIZE_START", "WINDOW_SIZE_END", "WINDOW_SIZE_STEP", "PLS_COMPONENTS"]:
            if not isinstance(config[key], int) or config[key] <= 0:
                raise ValueError(f"{key} must be a positive integer.")
        elif key in ["ALPHA_THRESHOLD"]:
            if not isinstance(config["ALPHA_THRESHOLD"], (int, float)) or not 0 < config["ALPHA_THRESHOLD"] < 1:
                raise ValueError("ALPHA_THRESHOLD must be a float between 0 and 1.")
        elif key in ["CHEMICAL_SUBSTANCES"]:
            if not config["CHEMICAL_SUBSTANCES"]:
                raise ValueError("CHEMICAL_SUBSTANCES list cannot be empty.")
            if not isinstance(config["CHEMICAL_SUBSTANCES"], list) or not all(isinstance(x, int) for x in config["CHEMICAL_SUBSTANCES"]):
                raise ValueError("CHEMICAL_SUBSTANCES must be a list of integers.")
            if len(config["CHEMICAL_SUBSTANCES"]) == 0:
                raise ValueError("CHEMICAL_SUBSTANCES list cannot have length 0. This may affect the analysis.")
        elif key == "SHUFFLE_DATA":
            if not isinstance(config[key], bool):
                raise ValueError("SHUFFLE_DATA must be a boolean.")

    # Additional checks
    if config["WINDOW_SIZE_START"] >= config["WINDOW_SIZE_END"]:
        raise ValueError("WINDOW_SIZE_START must be less than WINDOW_SIZE_END.")
    if config["WINDOW_SIZE_STEP"] > (config["WINDOW_SIZE_END"] - config["WINDOW_SIZE_START"]):
        raise ValueError("WINDOW_SIZE_STEP must be less than the range of window sizes.")

    return config

# Validate and update the configuration
try:
    CONFIG = validate_and_set_defaults(DEFAULT_CONFIG)
    print("Configuration is valid.")
    for key, value in CONFIG.items():
        print(f"{key}: {value}")
except ValueError as e:
    print(f"Configuration error: {e}")