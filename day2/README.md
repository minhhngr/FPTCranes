# Day2

## Pandas Series, Creation, Indexing and Operations

- 1D
  - Series Creation
  - Series Indexing

- 2D
- Creating a Pandas Series
- Indexing and Slicing in Pandas Series
- Adding, Deleteing, and Renaming in Pandas DataFrame
  - df.rename(columns={"old_name": "new_name"}, inplace=True)
  - df.drop("column_name", axis=1, inplace=True)
  - df.drop("row_index", axis=0, inplace=True)
  - df['new_column'] = values_list
  - df['new_column'] = df['existing_column'] * 2
  - df['new_column'] = df['existing_column1'] + df['existing_column2']
  - ...
- Operations on Pandas Series and DataFrame
  - Arithmetic Operations
  - Statistical Operations
  - Applying Functions
  - Handling Missing Data

## Handling Missing Data in Pandas

- isnull()
- fillna()
- dropna()


