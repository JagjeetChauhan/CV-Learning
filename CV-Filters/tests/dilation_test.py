import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from src.core.dilation import dilation
from src.utils.image_utils import load_image

# Load image
image = load_image("Data/Inputs/cat.jpg")

# Convert to numpy array
image_array = np.array(image)

# Convert to binary
binary = np.where(image_array > 128, 255, 0)

# Apply dilation
output = dilation(image_array, kernel_size=3)

# Display original image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image_array, cmap="gray")

# Display dilated image
plt.subplot(1, 2, 2)
plt.title("Dilated")
plt.imshow(output, cmap="gray")

plt.show()