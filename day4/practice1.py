# Vẽ 2 đường thằng y = 2x, y = 2x+3
import matplotlib.pyplot as plt

x = range(10)
y1 = [2 * i for i in x]
y2 = [2 * i + 3 for i in x]

plt.plot(x, y1, label="y = 2x")
plt.plot(x, y2, label="y = 2x + 3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("plot.png")
