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
    