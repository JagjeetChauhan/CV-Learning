"""
What is Dilation?

Dilation:

expands bright regions
thickens objects

Useful for:

segmentation
OCR
mask cleanup
Structuring Element

Kernel in morphology called:

structuring element
"""

import numpy as np

from src.core.padding import zero_padding

def dilation(
    image: np.ndarray,
    kernel_size: int = 11
) -> np.ndarray:

    pad = kernel_size // 2

    padded = zero_padding(image, pad)

    output = np.zeros_like(image)

    for y in range(image.shape[0]):

        for x in range(image.shape[1]):

            patch = padded[
                y:y + kernel_size,
                x:x + kernel_size
            ]

            output[y, x] = np.max(patch)

    return output