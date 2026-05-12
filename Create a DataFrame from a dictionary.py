#* Create a DataFrame from a dictionary
#* Create a DataFrame from a list of dictionaries
#* Inspect with head(), info(), shape()
import pandas as pd


def create_df_from_dic(dictt):
    df= pd.DataFrame(dictt)
    return df

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
data2=[
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Alice", "age": 20, "grade": "A"}
]

df = create_df_from_dic(data)
print(df)   
print("Head of the DataFrame: ,n", df.head())  # Display the first few rows of the DataFrame
print("Information about the DataFrame: ,n", df.info())  # Display information about the DataFrame
print("Shape of the DataFrame: ,n", df.shape)  # Display the shape of the DataFrame (number of rows and columns)

#Time Complexity: The time complexity of creating a DataFrame from a dictionary using `pd.DataFrame()` is O(n), where n is the number of key-value pairs in the dictionary. This is because the function needs to iterate through each key-value pair to construct the DataFrame.
#Space Complexity: The space complexity of creating a DataFrame from a dictionary is also O(n), where n is the number of key-value pairs in the dictionary. This is because the DataFrame will require space to store the data from the dictionary, and the amount of space needed will depend on the size of the dictionary and the structure of the data. Additionally, there may be some overhead associated with the DataFrame object itself, but this is generally considered to be O(1) since it does not scale with the size of the input data.
df1 = create_df_from_dic(data2)
print(df1)   
#T  ime Complexity: The time complexity of creating a DataFrame from a list of dictionaries using `pd.DataFrame()` is O(n), where n is the number of dictionaries in the list. This is because the function needs to iterate through each dictionary to construct the DataFrame.
#Space Complexity: The space complexity of creating a DataFrame from a list of dictionaries is also O(n), where n is the number of dictionaries in the list. This is because the DataFrame will require space to store the data from the list of dictionaries, and the amount of space needed will depend on the size of the list and the structure of the data. Additionally, there may be some overhead associated with the DataFrame object itself, but this is generally considered to be O(1) since it does not scale with the size of the input data.
