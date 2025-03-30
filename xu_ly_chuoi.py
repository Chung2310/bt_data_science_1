#không có dữ liệu tên hãng lên sẽ thay thể bằng mã bằng chữ của Sân Bay Đi 
import pandas as pd

# Đọc file CSV
file_path = "Airline_dataset.csv"
df = pd.read_csv(file_path)

df = df["ORIGIN_AIRPORT"].str.lower()

print(df.head)