import numpy as np
import cv2
import os
from tests.conv_from_scratch import elementwise_multiplication
from src.filters.kernels import edge_filter, box_blur_filter, sharpen_filter, gaussian_blur, sobel_x, sobel_y
from src.core.convolution import convolve2d
from src.utils.image_utils import load_image, show_image

image = load_image("Data/Inputs/cat.jpg")

"""
For Kernel size: K
Padding: P
Image size: N
Output size = [(N-K+2P)/S] + 1
Where S -> Stride
"""

output = convolve2d(
    image,
    box_blur_filter,
    padding=1
)

print("Image Shape before padding: ",image.shape)
print("Image shape after padding: ",output.shape)
show_image(output, title="Edge Filter")

# Save image:-
# Convert to uint8
output = output.clip(0, 255).astype("uint8")

# Output folder
output_folder = r"C:\Users\jagje\AI hub\CV-Learning\CV-Filters\Data\Outputs"

# Create folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Output path
output_path = os.path.join(output_folder, "box_blur_filter_output.jpg")

# Save image
cv2.imwrite(output_path, output)

print(f"Saved at: {output_path}")