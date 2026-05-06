#* Count rows matching a category

#output
""" [
    {"name": "Laptop", "category": "Electronics", "price": "800", "stock": "10"},
    {"name": "Phone", "category": "Electronics", "price": "500", "stock": "25"},
    {"name": "Shirt", "category": "Clothing", "price": "40", "stock": "50"},
    {"name": "Jeans", "category": "Clothing", "price": "60", "stock": "30"},
    {"name": "Book", "category": "Education", "price": "20", "stock": "100"},
    {"name": "Headphones", "category": "Electronics", "price": "150", "stock": "15"}
] """
import csv

def read_data_from_csvfile(file_path):
    counter=0
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
             # Print each row as a dictionary
            if row.get("category") == "Electronics": 
                counter+=1
    return counter
file_path = 'data.csv'  # Replace with your file path
data = read_data_from_csvfile(file_path)
print(data)  # Output the contents of the file
# Time complexity: O(n), where n is the size of the file. This is because we read the entire file content once, which takes O(n) time.
# Space complexity: O(n), where n is the size of the file. This is because we store the entire file content in memory as a string, which can take up to O(n) space. However, if we consider the file content as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the string reference and temporary variables used during the file reading process.  