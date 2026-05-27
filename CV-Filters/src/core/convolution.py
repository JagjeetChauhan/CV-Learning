import numpy as np
from src.core.padding import zero_padding

def convolve2d(image: np.ndarray,
               kernel: np.ndarray,
               stride: int = 1,
               padding: int = 0) -> np.ndarray:
    
    """
    Perform manual 2D convolution.

    Args:
        image: Grayscale input
        Kernel: Convolution Kernel

    Returns:
        Feature Map
    """

    # Flip kernel for true convolution
    kernel = np.flipud(np.fliplr(kernel))
    kernel_height, kernel_width = kernel.shape
    padded_image = zero_padding(image, padding)
    image_height, image_width = padded_image.shape

    # Output dimensions
    output_height = ((image_height - kernel_height)//stride) + 1
    output_width = ((image_width - kernel_width)//stride) + 1

    output = np.zeros((output_height, output_width))

    # Sliding window
    for y in range(0, output_height):
        for x in range(0, output_width):

            # Extract local region

            y_start = y * stride
            y_end = y_start + kernel_height

            x_start = x * stride
            x_end = x_start + kernel_width

            region = padded_image[
                y_start:y_end,
                x_start:x_end
            ]

            # Element-wise multiplication
            multiplied = region * kernel

            # Summation
            value = np.sum(multiplied)

            # Store output
            output[y,x] = value

            # PRINT ONLY FOR ONE PIXEL
            # if y == 0 and x == 0:
            #     print("=== DEBUG FOR OUTPUT PIXEL (0,0) ===")

            #     print("\nImage Patch:")
            #     print(region)

            #     print("\nKernel:")
            #     print(kernel)

            #     print("\nElement-wise Multiplication:")
            #     print(multiplied)

            #     print("\nSummation:")
            #     print(value)
    
    return output

"""
IMPORTANT — Convolution vs Correlation

True convolution flips kernel.

Most deep learning libraries actually use:

cross-correlation
NOT strict convolution

But mathematically:

convolution includes flipping.

This distinction matters in research.
"""