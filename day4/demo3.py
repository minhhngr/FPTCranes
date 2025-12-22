import matplotlib.pyplot as plt
import numpy as np

months = range(1, 13)
revenue = [20, 22, 25, 23, 26, 28, 30, 29, 31, 33, 35, 40]


plt.plot(months, revenue)
plt.xlabel("Month")
plt.ylabel("Revenue (in thousands)")
plt.title("Monthly Revenue")
plt.savefig("monthly_revenue.png")

# Tìm được thẳng tốt nhất
# y = ax + b

coefficients = np.polyfit(list(months), revenue, 1)
line = np.poly1d(coefficients)

plt.plot(months, revenue, label="Revenue")
plt.plot(months, line(months), label="Best Line", linestyle="--")
plt.xlabel("Month")
plt.ylabel("Revenue (in thousands)")
plt.title("Monthly Revenue with Best Line")
plt.legend()
plt.savefig("monthly_revenue_with_fit.png")

print("Coefficients (a, b):", coefficients)
