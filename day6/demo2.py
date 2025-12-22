import numpy as np
import matplotlib.pyplot as plt

# left-skewed distribution
left_data = np.random.beta(a=5, b=2, size=1000) * 1000

# right-skewed distribution
right_data = np.random.beta(a=2, b=5, size=1000) * 1000

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot left-skewed data
axes[0].hist(left_data, bins=30, color="red", alpha=0.7)
axes[0].set_title("Histogram of Left-Skewed Distributed Data")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")

# Plot right-skewed data
axes[1].hist(right_data, bins=30, color="blue", alpha=0.7)
axes[1].set_title("Histogram of Right-Skewed Distributed Data")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram.png")
