import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({"Age": [25, 32, 47, 51], "Income": [5000, 60000, 80000, 90000]})

scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(df_scaled)
