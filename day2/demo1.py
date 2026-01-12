import pandas as pd

series1 = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print("Series:\n", series1)

print()
series2 = pd.Series([10, 20, 30], index=["mark1", "mark2", "mark3"])
print("Series 2:\n", series2)

print()
print("s2[1]", series2.iloc[1])
print("s2[mark1]", series2["mark1"])
