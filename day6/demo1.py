import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(data, bins=30, color="blue", alpha=0.7)
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
