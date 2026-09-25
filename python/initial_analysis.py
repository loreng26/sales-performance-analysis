import pandas as pd

df = pd.read_csv("data/sales_performance_project.csv")

print("Dataset shape:", df.shape)

print("\nFirst rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicated rows:", df.duplicated().sum())