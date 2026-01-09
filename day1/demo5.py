import numpy as np

tmp = np.array(range(1, 13))

print(tmp.reshape(3, 4))
print(tmp.reshape(-1, 3))  # auto determine number of rows
print(tmp.reshape(2, -1))  # auto determine number of columns
