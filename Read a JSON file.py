#* Read a JSON file
import json
def read_json(file_path):
    with open(file_path, 'r') as file:
        read_json_reader = json.load(file)
    return read_json_reader


file_path = 'data.json'  # Replace with your file path
data = read_json(file_path)
print(data) 

#Time Complexity.The time complexity of reading a JSON file using the `json.load()` function is O(n), where n is the size of the JSON file. This is because the function needs to read through the entire file to parse it into a Python object.
#Space Complexity.The space complexity of reading a JSON file using the `json.load()` function is also O(n), where n is the size of the JSON file. This is because the function creates a Python object in memory that represents the entire contents of the JSON file. The amount of memory used will depend on the size and structure of the JSON data.   

