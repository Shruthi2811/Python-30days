#* Fill nulls with default values based on data type

import pandas as pd

def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt)
    df= df.fillna(value={"name": "Unknown", "age": 0.0, "department": "Unknown", "salary": 0.0})
    return df

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, None, 30, 28, None],
    "department": ["HR", "IT", None, "Finance", "HR"],
    "salary": [50000, 60000, None, 70000, None]
}
df = create_df_from_dic(data)
print(df)

