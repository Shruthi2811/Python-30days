#* Standardize text using str.lower(), str.strip()
import pandas as pd

def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt)
    df['full_name'] = df['first_name'].str.strip() + " " + df['last_name'].str.strip()
    df['department_upper'] = df['department'].str.strip().str.upper()
    df['department_lower'] = df['department'].str.strip().str.lower()
    return df

data = {
    "first_name": [" Alice", "Bob ", " Charlie ", "David", " Eva "],
    "last_name": ["Smith ", " Johnson", "Brown", " Wilson ", "Davis"],
    "department": [" HR", "it ", " Finance ", "IT", " hr "],
    "salary": [50000, 60000, 70000, 65000, 52000]
}
df = create_df_from_dic(data)
print(df)