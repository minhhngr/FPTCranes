import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    "CustomerID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   11, 12, 13, 14, 15, 16, 17, 18, 19, 20],

    "Gender": ["Male", "female", "FEMALE", " Male ", np.nan,
               "Female", "MALE", "male", "Female", " FEMALE ",
               "male", "Female", np.nan, "MALE", "female",
               "Male", "FEMALE", "female ", "MALE", np.nan],

    "Age": [19, 22, 35, 40, 23,
            50, 18, 60, 29, np.nan,
            45, 33, 27, 120, 38,
            41, 26, np.nan, 34, 21],

    "AnnualIncome": [15000, 30000, np.nan, 58000, 48000,
                     100000, 12000, 90000, 52000, 61000,
                     np.nan, 45000, 39000, 800000, 54000,
                     62000, 41000, 37000, np.nan, 28000],

    "SpendingScore": [39, 81, 6, np.nan, 77,
                      40, 90, 20, 65, 50,
                      55, np.nan, 72, 99, 45,
                      60, np.nan, 30, 85, 75],

    "City": ["Hanoi", "hcm", "DaNang", " HANOI ", "Hcm",
             "haNoi", "DANANG", "HCM", "Hanoi", "danang ",
             "hCm", "HANOI", "hcm", "HaNoi", "Danang",
             "HCM ", "Hanoi", " DaNang", "HCM", "hanoi"],

    "Purchased": ["No", "YES", "no", "Yes", " yes ",
                  "NO", "Yes", "no", "YES", "No",
                  "yes", "NO", "Yes", "YES", "no",
                  "Yes", "No", "NO", "YES", " no "]
}

df = pd.DataFrame(data)

# =========================
# 1️⃣ Text Cleaning & Standardization
# =========================

cols = ["Gender", "City", "Purchased"]
for col in cols:
    df[col] = df[col].str.strip().str.lower()

print()
print("Text Cleaning & Standardization")
print("-" * 30)
print(df[cols].head())

# =========================
# 2️⃣ Handling Missing Values
# =========================

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["AnnualIncome"] = df["AnnualIncome"].fillna(df["AnnualIncome"].median())
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["SpendingScore"] = df.groupby("Gender")["SpendingScore"].transform(
    lambda x: x.fillna(x.mean())
)

print()
print("Handling Missing Values")
print("-" * 30)
print(df[["Age", "AnnualIncome", "SpendingScore", "Gender"]].isna().sum())

# =========================
# 3️⃣ Encoding Categorical Variables
# =========================

df["Gender"] = df["Gender"].map({"male": 0, "female": 1})
df["Purchased"] = df["Purchased"].map({"no": 0, "yes": 1})
city_dummies = pd.get_dummies(df["City"], prefix="City")
df = pd.concat([df.drop(columns=["City"]), city_dummies], axis=1)

print()
print("Encoding Categorical Variables")
print("-" * 30)
print(df.head())

# =========================
# 4️⃣ Feature Scaling
# =========================

num_cols = ["Age", "AnnualIncome", "SpendingScore"]

before = df[num_cols].agg(["min", "max", "mean", "std"])

minmax_scaler = MinMaxScaler()
minmax = df.copy()
minmax[num_cols] = minmax_scaler.fit_transform(df[num_cols])
minmax_stats = minmax[num_cols].agg(["min", "max", "mean", "std"])

standard_scaler = StandardScaler()
zscore = df.copy()
zscore[num_cols] = standard_scaler.fit_transform(df[num_cols])
zscore_stats = zscore[num_cols].agg(["min", "max", "mean", "std"])

print("-" * 30)
print("before (min/max/mean/std)")
print(before)

print("-" * 30)
print("min-max (min/max/mean/std)")
print(minmax_stats)

print("-" * 30)
print("z-score (min/max/mean/std)")
print(zscore_stats)


# =========================
# 5️⃣ Prepare Data for Machine Learning
# =========================

y = df["Purchased"]
X = df.drop(columns=["Purchased"])

print()
print("Prepared Data for Machine Learning")
print("-" * 30)
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)
