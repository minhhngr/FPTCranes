import pandas as pd
import numpy as np

df = pd.DataFrame(
    dict(
        order_id=[1, 2, 3, 4, 5],
        order_date=[
            "2024-01-01",
            "2024/01/02",
            "2024-01-03",
            None,
            "2024/01/05",
        ],
        amount=[100, 150, 200, None, 300],
        customer=["A", "B", "C", "D", "E"],
    )
)

# chuẩn hóa dữ liệu
df["order_date"] = pd.to_datetime(df["order_date"], format="%Y/%m/%d",errors="coerce")
df["amount"] = df["amount"].fillna(df["amount"].mean())
df["customer"] = df["customer"].str.upper()

print("DataFrame sau khi chuẩn hóa dữ liệu:")
print("-" * 40)
print(df)

df['day'] = df['order_date'].dt.day

# outliers
q1 = df["amount"].quantile(0.25)
q3 = df["amount"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df["amount"] < lower_bound) | (df["amount"] > upper_bound)]
print("\nOutliers trong cột 'amount':")
print("-" * 40)
print(outliers)
