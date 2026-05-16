import cv2
import matplotlib.pyplot as plt

def load_and_show_image(image_path):
    # Load grayscale image
    image = cv2.imread(image_path, 0)

    if image is None:
        print("Failed to load image")
        return None

    # Display image
    plt.imshow(image, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    return image