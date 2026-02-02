import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame(
    {"Age": [25, 30, 35, 40, 45], "Income": [50000, 60000, 70000, 80000, 90000]}
)

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print(df_scaled)
