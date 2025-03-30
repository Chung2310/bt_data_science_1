import pandas as pd

# Đọc file CSV
file_path = "Airline_dataset.csv"
df = pd.read_csv(file_path)

df_price = df.groupby("AIRLINE_ID")["PRICE"].mean()

print(df_price.head)