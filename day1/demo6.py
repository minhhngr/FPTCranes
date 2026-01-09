# stacking
import numpy as np

tmp = np.array([1, 2, 3])
tmp_b = np.array([4, 5, 6])

print("Vertical Stacking\n", np.vstack((tmp, tmp_b)))  # vertical stack
print("Horizontal stacking", np.hstack((tmp, tmp_b)))  # horizontal stack

print("Column stacking", np.stack((tmp, tmp_b), axis=1))  # column stack

tmp_c = np.array([[1, 2, 3], [7, 8, 9]])
tmp_d = np.array([[4, 5, 6], [10, 11, 12]])

print("Stacking along axis 0\n", np.stack((tmp_c, tmp_d), axis=0))  # stacking along axis 0
print("Stacking along axis 1\n", np.stack((tmp_c, tmp_d), axis=1))  # stacking along axis 1
