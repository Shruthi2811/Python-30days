#Group a list of dictionaries by a key
students = [
    {"name": "Alice", "department": "CS", "age": 20},
    {"name": "Bob", "department": "Math", "age": 21},
    {"name": "Charlie", "department": "CS", "age": 22},
    {"name": "David", "department": "Math", "age": 20},
    {"name": "Eva", "department": "Physics", "age": 23}
]

group_key = "department"
grouped_students = {}
def group_by_key(lst, key):
    for item in lst:
        group_value = item[key]     
        if group_value not in grouped_students:
            grouped_students[group_value] = []
        grouped_students[group_value].append(item)
    return grouped_students
result = group_by_key(students, group_key)
print(result)
# Output: {'CS': [{'name': 'Alice', 'department': 'CS', 'age': 20}, {'name': 'Charlie', 'department': 'CS', 'age': 22}], 'Math': [{'name': 'Bob', 'department': 'Math', 'age': 21}, {'name': 'David', 'department': 'Math', 'age': 20}], 'Physics': [{'name': 'Eva', 'department': 'Physics', 'age  : 23}]}
# Time complexity: O(n), where n is the number of dictionaries in the input list. This is because we iterate through the list of dictionaries once to group them by the specified key, which takes O(n) time.
# Space complexity: O(m), where m is the number of unique values for the specified key in the input list. This is because we create a new dictionary to store the grouped dictionaries, which can take up to O(m) space in the worst case if all dictionaries have unique values for the specified key. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new dictionary reference and temporary variables used during the grouping process.    




