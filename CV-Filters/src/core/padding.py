import numpy as np

"""
Without padding:

image shrinks
border information lost
"""

def zero_padding(
        image: np.ndarray,
        pad_size: int
) -> np.ndarray:
    """
    Add zero padding manually.
    """
    height, width = image.shape
    padded_height = height + 2 * pad_size
    padded_width = width + 2 * pad_size

    padded_image = np.zeros(
        (padded_height, padded_width), dtype=image.dtype
    )

    padded_image[
        pad_size:pad_size + height,
        pad_size:pad_size + width
    ] = image
    return padded_image