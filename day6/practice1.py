import pandas as pd

data = {
    "Age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 40],
    "AnnualIncome": [15, 18, 45, 80, 60, 90, 85, 100, 110, 50],  # triệu/năm
    "CreditScore": [520, 580, 650, 720, 700, 750, 730, 780, 800, 680],
    "YearsOfExperience": [1, 2, 10, 25, 20, 30, 28, 35, 40, 15],
    "NumberOfPurchases": [3, 5, 12, 20, 18, 25, 22, 30, 35, 15],
    "SpendingScore": [20, 25, 60, 85, 75, 90, 88, 95, 98, 70],
}
df = pd.DataFrame(data)

corr = df.corr()
corr_target = corr["SpendingScore"].sort_values(ascending=False)
print("-" * 30)
print(corr_target)


# => cao nhất: CreditScore, thấp nhất: NumberOfPurchases
credit_corr = corr_target["CreditScore"]
purchase_corr = corr_target["NumberOfPurchases"]
print("-" * 30)
print(
    f"Correlation with SpendingScore - CreditScore: {credit_corr}, NumberOfPurchases: {purchase_corr}"
)

mean_values = df.mean()
std_values = df.std()
print("-" * 30)
print("Mean values:\n", mean_values)
print("-" * 30)
print("Standard Deviation values:\n", std_values)

# mean của mỗi feature

# std xấp xỉ bao nhiêu

# so sánh min-max vs Z-Score
min_max_normalized = (df - df.min()) / (df.max() - df.min())
z_score_normalized = (df - mean_values) / std_values
print("-" * 30)
print("Min-Max Normalized Data:\n", min_max_normalized)
print("-" * 30)
print("Z-Score Normalized Data:\n", z_score_normalized)

# Nên chuẩn hóa trước hay feature selection trước?



# Nếu dataset có outlier rất lớn: chọn min-max hay z-score, có xử lý trước không
