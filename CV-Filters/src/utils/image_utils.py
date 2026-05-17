import cv2
import matplotlib.pyplot as plt
import numpy as np


def load_image(image_path: str) -> np.ndarray:
    """
    Load grayscale image.

    Args:
        image_path: Path to image

    Returns:
        Grayscale image
    """

    image = cv2.imread(image_path, 0)

    if image is None:
        raise FileNotFoundError(
            f"Failed to load image: {image_path}"
        )

    return image


def show_image(image: np.ndarray,
               title: str = "Image") -> None:
    """
    Display image using matplotlib.

    Args:
        image: Input image
        title: Plot title
    """

    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis("off")
    plt.show()


# Load image
# image = load_image("../..//Data/Inputs/cat.jpg")

# Display image
# show_image(image, "Original Image")