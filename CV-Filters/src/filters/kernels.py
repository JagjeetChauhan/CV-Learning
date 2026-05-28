import numpy as np

# Edge Detection
edge_filter = np.array([
    [-1, -1, -1],
    [-1,  4, -1],
    [-1, -1, -1]
])

"""
Why Derivatives Detect Edges

If intensity is constant:

f(x)=10

Derivative:

df/dx = 0

No change → no edge.

If intensity changes sharply:

10→250

Derivative becomes large.

Large derivative = edge.
"""

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

"""
Detects:

horizontal intensity change
vertical edges
"""

# Sobel Y
sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

"""
Detects:

vertical intensity change
horizontal edges
"""

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