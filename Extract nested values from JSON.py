#* * Extract nested values from JSON file
import json
def read_json(file_path):
    with open(file_path, 'r') as file:
        read_json_reader = json.load(file)
        name = read_json_reader.get('details').get('name')
        age = read_json_reader.get('details').get('age')
        math_score = read_json_reader.get('marks').get('math')
    return name,age,math_score


file_path = 'data.json'  # Replace with your file path
data = read_json(file_path)
print(data)  # Print the extracted values as a tuple
print(data[0])  # Print the extracted name
print(data[1])  # Print the extracted age
print(data[2])  # Print the extracted math score

#Time Complexity.The time complexity of extracting nested values from a JSON file using the `json.load()` function and accessing nested keys is O(n), where n is the size of the JSON file. This is because the function needs to read through the entire file to parse it into a Python object, and then access the nested keys takes constant time O(1) for each key access.
#Space Complexity.The space complexity of extracting nested values from a JSON file using the `json.load()` function is O(n), where n is the size of the JSON file. This is because the function creates a Python object in memory that represents the entire contents of the JSON file. The amount of memory used will depend on the size and structure of the JSON data, and the additional space used for storing the extracted values is O(1) since it only stores a fixed number of values (name, age, math_score).

