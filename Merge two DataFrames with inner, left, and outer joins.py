#* Merge two DataFrames with inner, left, and outer joins
#* Understand what unmatched rows look like
#* Practice with customer and order datasets
import pandas as pd

def create_df_from_dic(dict1, dict2):
    df1= pd.DataFrame(dict1)
    df2= pd.DataFrame(dict2)
    df3=df1.merge(df2, on='customer_id',how="inner")
    df4=df1.merge(df2, on='customer_id',how="right")
    df5=df1.merge(df2, on='customer_id',how="left")
    df6=df1.merge(df2, on='customer_id',how="outer")
    return df3,df4,df5,df6

customers = {
    "customer_id": [1, 2, 3, 4],
    "customer_name": ["Alice", "Bob", "Charlie", "David"]
}

orders = {
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 2, 5],
    "amount": [250, 400, 150, 300]
}
df = create_df_from_dic(customers,orders)
print("Inner Join =", df[0])
print("Right Join =", df[1])
print("Left Join =", df[2])
print("Outer Join =", df[3])