#* * Extract nested values from JSON file
import json
def read_json(file_path):
    cleaned_json=[]
    with open(file_path, 'r') as file:
        read_json_reader = json.load(file)
        for row in read_json_reader:
            name = row.get('details').get('name')
            age = row.get('details').get('age')
            math_score = row.get('marks').get('math')
            cleaned_json.append({"name": name, "city": row.get('details').get('address').get('city'), "math": math_score})
    return cleaned_json

file_path = 'data2.json'  # Replace with your file path
data = read_json(file_path)
print(data)  # Print the extracted values as a tuple

#expected output
#[{"name": "Alice", "city": "Seattle", "math": 95}, {"name": "Bob", "city": "Boston", "math": 89}, {"name": "Charlie", "city": "Chicago", "math": 92}]