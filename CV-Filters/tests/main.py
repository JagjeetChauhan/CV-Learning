from src.utils.image_utils import load_image
from src.core.convolution import convolve2d

import numpy as np
import matplotlib.pyplot as plt

image = load_image("Data/Inputs/cat.jpg")

edge_kernel = np.array([
    [-1, -1, -1],
    [-1, 4, -1],
    [-1, -1, -1]
])

output = convolve2d(image, edge_kernel)

plt.imshow(output, cmap='gray')
plt.title("Edge Detection")
plt.show()

