import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
image = cv2.imread("../../Data/Inputs/cat.jpg", 0)
if image is None:
    print("Failed to load image")

plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.show()