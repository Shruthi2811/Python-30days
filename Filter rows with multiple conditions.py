#* Filter rows with multiple conditions

import pandas as pd

def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt)
    #Aproach1
    #return df[(df['Age'] > 25) & (df['Name'] == 'Charlie')]  # Select rows where the 'Age' column is greater than 25 and the 'City' column is 'Chicago'
    #Aproach2
    return df.query('Age > 25 and Name == "Charlie"')  # Select rows where the 'Age' column is greater than 25 and the 'City' column is 'Chicago'
    
    data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
data2=[
    {"Name": "Charlie", "Age": 20, "Grade": "A"},
    {"Name": "Alice", "Age": 20, "Grade": "A"}
]

df = create_df_from_dic(data)
print(df)   
print("Head of the DataFrame: ,n", df.head())  # Display the first few rows of the DataFrame
print("Information about the DataFrame: ,n", df.info())  # Display information about the DataFrame
print("Shape of the DataFrame: ,n", df.shape)  # Display the shape of the DataFrame (number of rows and columns)

df1 = create_df_from_dic(data2)
print(df1)   
