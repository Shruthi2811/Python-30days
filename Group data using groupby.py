#* Group data using groupby
import pandas as pd

def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt)
    newdf = df.groupby('region')['sales_amount'].agg(['sum', 'count', 'mean'])
    newdf['mean'] = newdf['mean'].round(2)
    return newdf

data = {
    "salesperson": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "region": ["East", "West", "East", "West", "East", "West"],
    "sales_amount": [500, 700, 300, 900, 400, 600]
}
df = create_df_from_dic(data)
print(df)
