#* Remove duplicate rows
import pandas as pd

def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt)
    df=df.sort_values(by=['department','salary'],ascending=[True,False])
    df=df.drop_duplicates()
    return df

data = {
    "employee_id": [101, 102, 101, 103, 104, 104],
    "name": ["Alice", "Bob", "Alice", "Charlie", "David", "David"],
    "department": ["HR", "IT", "HR", "Finance", "IT", "IT"],
    "salary": [50000, 60000, 52000, 70000, 65000, 65000],
    "updated_at": [
        "2024-01-10 09:00:00",
        "2024-01-11 10:30:00",
        "2024-02-15 14:00:00",
        "2024-01-12 08:45:00",
        "2024-01-20 16:00:00",
        "2024-01-20 16:00:00"
    ]
}
df = create_df_from_dic(data)
print(df)