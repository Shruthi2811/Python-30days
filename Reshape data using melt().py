#Reshape data using melt() 

import pandas as pd

def cleandata(data):
    df=pd.DataFrame(data)
    print(df)
    df=df.melt(
        id_vars='product',
        value_vars=['Jan', 'Feb', 'Mar'],
        var_name='month',
        value_name='sales'
    )
    return df


data = {
    "product": ["Laptop", "Phone", "Tablet"],
    "Jan": [120, 200, 150],
    "Feb": [130, 180, 160],
    "Mar": [140, 210, 170]
}
df=cleandata(data)
print(df)