import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import kurtosis

df = pd.read_csv("sample_101_coffee_shop_revenue.csv")


# ve historgram (x: revenue, y: frequency)


plt.hist(df["Daily_Revenue"], bins=30, color="red", edgecolor="yellow")
plt.title("Histogram of Daily Revenue")
plt.xlabel("Daily Revenue")
plt.ylabel("Frequency")
plt.savefig("daily_revenue_histogram.png")

# compare mean with median, and draw conclusion
# calculate skew, kurtosis
# draw conclusion about distribution shape

mean_revenue = df["Daily_Revenue"].mean()
median_revenue = df["Daily_Revenue"].median()
skew_revenue = df["Daily_Revenue"].skew()
kurtosis_revenue = df["Daily_Revenue"].kurtosis()

plt.hist(df["Daily_Revenue"], bins=30, color="pink")
plt.axvline(mean_revenue, color="blue", linestyle="dashed", linewidth=1, label="Mean")
plt.axvline(
    median_revenue, color="green", linestyle="dashed", linewidth=1, label="Median"
)
plt.title("Histogram of Daily Revenue with Mean and Median")

plt.xlabel("Daily Revenue")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("daily_revenue_histogram_with_mean_median.png")

print(f"Mean Daily Revenue: {mean_revenue}")
print(f"Median Daily Revenue: {median_revenue}")
print(f"Skewness of Daily Revenue: {skew_revenue}")
print(f"Kurtosis of Daily Revenue: {kurtosis_revenue}")

if skew_revenue > 0:
    print("The distribution is right-skewed.")
elif skew_revenue < 0:
    print("The distribution is left-skewed.")
else:
    print("The distribution is symmetric.")
if kurtosis_revenue > 3:
    print("The distribution is leptokurtic (heavy-tailed).")
elif kurtosis_revenue < 3:
    print("The distribution is platykurtic (light-tailed).")
else:
    print("The distribution is mesokurtic (normal-tailed).")

# draw boxplot for daily revenue
plt.boxplot(df["Daily_Revenue"], vert=False)
plt.title("Boxplot of Daily Revenue")
plt.xlabel("Daily Revenue")
plt.savefig("daily_revenue_boxplot.png")
