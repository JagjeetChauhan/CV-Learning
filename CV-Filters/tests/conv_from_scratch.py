import numpy as np

def elementwise_multiplication(
        image_patch: np.ndarray,
        kernel: np.ndarray
) -> float:
    """
    Perform element-wise multiplication and summation.
    """
    multiplied = image_patch * kernel

    return np.sum(multiplied)