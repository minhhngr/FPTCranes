import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
})

encoder = OneHotEncoder(sparse_output=False)
df_encoded = pd.DataFrame(encoder.fit_transform(df), columns=encoder.get_feature_names_out(["City"]))
print(df_encoded)