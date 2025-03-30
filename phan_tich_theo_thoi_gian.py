import pandas as pd

file_path = "Airline_dataset.csv"
df = pd.read_csv(file_path)

# Chuyển đổi FL_DATE và xử lý lỗi
df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], format="%m/%d/%y", errors="coerce")

# Loại trùng lặp nếu cần
df = df.drop_duplicates()

# Đặt chỉ số và đếm
df.set_index("FL_DATE", inplace=True)

df_price = df.resample("ME").size()

print(df_price)