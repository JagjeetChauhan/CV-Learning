import numpy as np

# Edge Detection
edge_filter = np.array([
    [-1, -1, -1],
    [-1,  4, -1],
    [-1, -1, -1]
])

# Sharpen
sharpen_filter = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

# Box Blur
box_blur_filter = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

# Sobel X
sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

# Sobel Y
sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

# Gaussian
gaussian_blur = (1/16) * np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

# Prewitt X
PREWITT_X = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

# Prewitt Y
PREWITT_Y = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])