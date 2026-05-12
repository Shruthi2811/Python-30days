#* Use apply() on a column
import pandas as pd

def add_bonus(salary):
    return salary * 1.1  # Add a 10% bonus to the salary

def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt)
    df['full_name'] = df['first_name'].str.strip() + " " + df['last_name'].str.strip()
    df['salary_bonus'] = df['salary'].apply(add_bonus)  # Apply the add_bonus function to the 'salary' column
    #df['salary_bonus'] = df['salary'].apply(lambda x:x*1.1)  # Apply the add_bonus function to the 'salary' column
    return df

data = {
    "first_name": [" Alice", "Bob ", " Charlie ", "David", " Eva "],
    "last_name": ["Smith ", " Johnson", "Brown", " Wilson ", "Davis"],
    "department": [" HR", "it ", " Finance ", "IT", " hr "],
    "salary": [50000, 60000, 70000, 65000, 52000]
}
df = create_df_from_dic(data)
print(df)