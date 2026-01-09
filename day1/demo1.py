import numpy as np

# 1D array
tmp_a = np.array([1, 2, 3, 4, 5])  # 1D array

# 2D array
tmp_b = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

# Shape: dimensions of the array
print(f"Shape of tmp_a: {tmp_a.shape}")  # Output: (5,)
print(f"Shape of tmp_b: {tmp_b.shape}")  # Output: (2, 3)

# Size: total number of elements
print(f"Size of tmp_a: {tmp_a.size}")    # Output: 5
print(f"Size of tmp_b: {tmp_b.size}")    # Output: 6

# dtype: data type of the elements
print(f"dtype of tmp_a: {tmp_a.dtype}")  # Output: int64 (or int32 depending on system
print(f"dtype of tmp_b: {tmp_b.dtype}")  # Output: int64 (or int32 depending on system

# ndim: number of dimensions
print(f"ndim of tmp_a: {tmp_a.ndim}")    # Output: 1
print(f"ndim of tmp_b: {tmp_b.ndim}")    # Output: 2
