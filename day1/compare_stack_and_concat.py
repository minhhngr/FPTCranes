import numpy as np

tmp = np.array([[1, 2, 3], [4, 5, 6]])
tmp_b = np.array([[7, 8, 9], [10, 11, 12]])

# Stacking vs Concatenation
print("Axis 0")
print("Stacking along axis 0\n", np.stack((tmp, tmp_b), axis=0))  # stacking along axis 0
print("Concatenation along axis 0\n", np.concatenate((tmp, tmp_b), axis=0))  # concatenate along rows

print()
print("Axis 1")
print("Stacking along axis 1\n", np.stack((tmp, tmp_b), axis=1))  # stacking along axis 1
print("Concatenation along axis 1\n", np.concatenate((tmp, tmp_b), axis=1))  # concatenate along columns