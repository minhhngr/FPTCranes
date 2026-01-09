import numpy as np

tmp = np.array([1, 2, 3])
tmp_b = np.array([4, 5, 6])


# Concat 
print("Concat", np.concatenate((tmp, tmp_b)))  # concatenate along rows

tmp_c = np.array([[1, 2, 3], [7, 8, 9]])
tmp_d = np.array([[4, 5, 6], [10, 11, 12]])
tmp_3 = np.array([[4, 5, 9], [10, 11, 13]])

print("Concat along axis 0\n", np.concatenate((tmp_c, tmp_d), axis=0))  # concatenate along rows
print("Concat along axis 1\n", np.concatenate((tmp_c, tmp_d), axis=1))  # concatenate along columns

# print(np.concatenate((tmp_c, tmp_d, tmp_3), axis=0).shape)
# print(np.concatenate((tmp_c, tmp_d,tmp_3), axis=1).shape)