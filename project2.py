import pandas as pd

df = pd.read_csv("students.csv")

# remove extra spaces from column names
df.columns = df.columns.str.strip()

print("First 5 rows of the data:")
print(df.head())

print("Last 5 rows of the data:")
print(df.tail())

print("Data Types:")
print(df.dtypes)

print("Mean Marks:", df["Marks"].mean())
print("Median Marks:", df["Marks"].median())
print("Min Marks:", df["Marks"].min())
print("Max Marks:", df["Marks"].max())
print("Count:", df["Marks"].count())