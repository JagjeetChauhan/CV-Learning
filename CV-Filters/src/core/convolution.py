import numpy as np

def convolve2d(image: np.ndarray,
               kernel: np.ndarray) -> np.ndarray:
    
    """
    Perform manual 2D convolution.

    Args:
        image: Grayscale input
        Kernel: Convolution Kernel

    Returns:
        Feature Map
    """

    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Output dimensions
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    output = np.zeros((output_height, output_width))

    # Sliding window
    for y in range(output_height):
        for x in range(output_width):

            # Extract local region
            region = image[
                y:y + kernel_height,
                x:x + kernel_width
            ]

            # Element-wise multiplication
            multiplied = region * kernel

            # Summation
            value = np.sum(multiplied)

            # Store output
            output[y,x] = value
    
    return output