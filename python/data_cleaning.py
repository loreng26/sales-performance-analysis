import pandas as pd

df = pd.read_csv("data/sales_performance_project.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Region"] = df["Region"].fillna("Unknown")

df = df.drop_duplicates()

print("Final shape:", df.shape)

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicated rows:", df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

df.to_csv("data/sales_performance_cleaned.csv", index=False)