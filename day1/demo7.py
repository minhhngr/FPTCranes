# splitting: 
import numpy as np

tmp = np.arange(10)
print(tmp)

print("Splitting into 3 parts:", np.split(tmp, 2))
print("Splitting at indices 3 and 7:", np.split(tmp, [5, 9]))