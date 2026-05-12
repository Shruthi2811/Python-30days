#Handle missing values in pandas
#Drop nulls

import pandas as pd

def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt).dropna()  # Drop rows with any null values
    return df

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, None, 30, 28, None],
    "department": ["HR", "IT", None, "Finance", "HR"],
    "salary": [50000, 60000, None, 70000, None]
}
df = create_df_from_dic(data)
print(df)

