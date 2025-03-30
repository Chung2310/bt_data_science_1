import pandas as pd
import numpy as np

# Đọc file CSV
file_path = "Airline_dataset.csv"
df = pd.read_csv(file_path)

#tổng giá trị null
#print(df.isnull().sum())

# điền vào các giá trị NaN trong cột "PRICE" bằng giá trị trung bình của cột PRICE được tính theo từng nhóm AIRLINE_ID
df["PRICE"] = df["PRICE"].fillna(df.groupby("AIRLINE_ID")["PRICE"].transform("mean"))

print(df.head)
