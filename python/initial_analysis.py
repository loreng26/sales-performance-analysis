import pandas as pd

df = pd.read_csv("data/sales_performance_project.csv")

duplicate_rows = df[df.duplicated()]

print("Lines/Columns: ", df.shape, "\n")
print("First Lines: ", "\n", df.head(), "\n")
print("Columns Types:", "\n", df.dtypes, "\n")
print("Missing Values:", "\n", df.isna().any(), "\n")
print("Duplicated Rows:", "\n", duplicate_rows)
