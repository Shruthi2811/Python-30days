
#Reshape data using pivot_table() 

import pandas as pd

def cleandata(data):
    df=pd.DataFrame(data)
    df=df.pivot_table(values=['Jan', 'Feb', 'Mar'],index='product')
    df.columns.name = 'month'
    return df


data = {
    "product": ["Laptop", "Phone", "Tablet"],
    "Jan": [120, 200, 150],
    "Feb": [130, 180, 160],
    "Mar": [140, 210, 170]
}
df=cleandata(data)
print(df)
