import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
    "Score": [85.5, 90.0, 88.5],
}

df = pd.DataFrame(data)
print(df)
