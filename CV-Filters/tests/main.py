import numpy as np
from conv_from_scratch import elementwise_multiplication

patch = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

kernel = np.array([
    [1,0,-1],
    [1,0,-1],
    [1,0,-1]
])

result = elementwise_multiplication(patch, kernel)

print("Result of element-wise multiplication and summation:", result)