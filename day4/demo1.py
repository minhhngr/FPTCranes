import pandas as pd
import numpy as np

printline = lambda: print("-" * 35)


df = pd.DataFrame(
    {
        "Name": ["A", "B", "C", "D"],
        "Math": [8, np.nan, 6, np.nan],
        "Physics": [
            np.nan,
            7,
            5,
            np.nan,
        ],
        "Chemistry": [7, 6, np.nan, np.nan],
    }
)
printline()
print("Raw:")
print(df)


# thresh: giữ lại nếu số giá trị đủ = n
# cột/hàng không đủ 2 dữ liệu => xóa sạch
printline()
df_clean = df.dropna(thresh=2)
print("Rows with at least 2 non-NA values:")
print(df_clean)


printline()
df_clean_1_1 = df.dropna(axis=1, thresh=1)
print("Columns with at least 1 non-NA value:")
print(df_clean_1_1)

# điền
df_filled = df.fillna(0)
printline()
print("Fill NA with 0:")
print(df_filled)

df_bfilled = df.bfill()  # điền ngược từ dưới lên --> lên trên
printline()
print("Back fill:")
print(df_bfilled)

df_ffilled = df.ffill()  # điền trên từ trên xuống --> xuống dưới
printline()
print("Forward Fill:")
print(df_ffilled)

df_ffilled_limit1 = df.ffill(limit=1)  # điền trên từ trên xuống --> xuống dưới, giới hạn 1 lần điền
printline()
print("Forward Fill with limit=1:")
print(df_ffilled_limit1)
