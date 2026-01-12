import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Class": ["10B", "10B", "10A", "10B", "10A"],
    "Subject": ["Math", "Science", "Math", "Science", "Math"],
    "Score": [8.5, np.nan, 7.0, 6.5, np.nan],
    "Age": [15, 16, 15, np.nan, 15],
}

df = pd.DataFrame(data)

# isnull: kiem tra du lieu bi thieu
print("Kiem tra du lieu bi thieu:")
print(df.isnull())

# đếm giá trị null mỗi cột
print("\nDem gia tri null moi cot:")
print(df.isnull().sum())

print("\nKiem tra cot nao co gia tri null:")
print(df.isnull().any())

print()
# df["Score"] = df["Score"].fillna(0)
# df["Score"].fillna(df["Score"].mean(), inplace=True)
# print(df)

print()
# df.fillna(0, inplace=True)
# explain: filling missing values with 0 may not be appropriate for all columns
df.fillna({"Score": df["Score"].mean(), "Age": df["Age"].median()}, inplace=True)
print(df)

# Xóa dữ liệu thiếu

# tmp = df.dropna()  # xóa dòng có giá trị null (all)
# print()
# print(tmp)
# print(df)
# df.dropna(how="all")  # xóa dòng nếu tất cả NaN

# df.dropna(axis=1)  # xóa cột có giá trị null
# df.dropna(subset=["Score"])  # xóa dòng có giá trị null ở cột Score

# sap xep du lieu
df.sort_values(by="Score", ascending=False, inplace=True)
print(df)

print(df.groupby("Class")["Score"].mean())  # tính điểm trung bình theo lớp

print(
    df.groupby("Class")["Score"].agg(["mean", "max", "min", "count"])
)  # tìm tuổi lớn nhất theo môn học


print(df.groupby("Class").agg({"Score": ["mean", "max"], "Age": ["mean", "min"]}))

# Đặt tên cho các cột kết quả
print(
    df.groupby("Class").agg(
        AvgScore=("Score", "mean"),
        MaxScore=("Score", "max"),
        AvgAge=("Age", "mean"),
        MinAge=("Age", "min"),
    )
)

print("-" * 20)
print(df)
print()
# print(df.groupby(["Class", "Subject"], as_index=False)["Score"].mean())
print()
print(df.groupby(["Class", "Subject"])["Score"].mean())
# print(
#     df.groupby(["Class", "Subject"]).agg(
#         AvgScore=("Score", "mean"), MaxAge=("Age", "max")
#     )
# )
