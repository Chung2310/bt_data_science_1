import pandas as pd

df1 = pd.read_csv("Airline_dataset.csv")
df2 = pd.read_csv(r"E:\HOC\Lập trình Python\baitapvenha\flights.csv")

df3 = pd.merge(df1, df2, on="AIRLINE_ID",how="inner")

print(df3)