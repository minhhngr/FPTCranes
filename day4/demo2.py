import pandas as pd
import numpy as np

printline = lambda: print("-" * 35)

# ----------------------
df = pd.DataFrame(
    {
        "Department": ["HR", "Finance", "IT", "Marketing"],
        "Salary": [50000, 60000, np.nan, 55000],
    }
)

print("Điền theo điều kiện:")
df["Salary"] = df["Salary"].fillna(df["Department"].map({"IT": 3000, "HR": 4000}))

printline()
print(df)

# ----------------------
df2 = pd.DataFrame(
    {
        "Department": ["HR", "Finance", "IT", "Marketing", "HR", "Finance", "Finance"],
        "Salary": [1000, 1200, 800, 900, 1100, 1200, 1200],
    }
)

printline()
df2["salary_norm"] = df2.groupby("Department")["Salary"].transform(
    lambda x: (x - x.mean()) / x.std()
)
print("Chuẩn hóa lương theo từng phòng ban:")
# std:
print(df2)
