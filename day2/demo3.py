import pandas as pd

data = [
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

df = pd.DataFrame(data, columns=["Name", "Age", "City"])
# print(df)

df.info()

print()

print(df.describe())

# xem du lieu
print()
print(df["Age"])
print(df[["Age", "City"]])

# loc vs iloc
print()
print(df.loc[0, "Name"])
print(df.loc[1:3, ["Name", "City"]])

# iloc
print()
print(df.iloc[0, 0])
print(df.iloc[1:3, [0, 2]])
print(df.iloc[:, 1])

# Add 1 column
df["Country"] = ["USA", "USA", "USA"]
print()
print(df)

# filter 
print()
print(df[df["Age"] > 25])

# xóa một cột
df.drop("Country", axis=1, inplace=True) # axis=1: xóa cột, axis=0: xóa hàng, inplace=True: thay đổi trực tiếp df
print(df)

# đổi tên
df.columns = ["Full Name", "Age", "Residence"]
print()
print(df)

