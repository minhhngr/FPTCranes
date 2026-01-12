import pandas as pd

df1 = pd.DataFrame({"A": ["A", "B"]})
df2 = pd.DataFrame({"B": ["C", "D"]})

print("-" * 30)
print(pd.concat([df1, df2]))
print("-" * 30)

df3 = pd.DataFrame({"B": [7, 8]})
print(pd.concat([df1, df3], axis=1))

print("-" * 30)
print(pd.concat([df1, df2], axis=0, ignore_index=True))