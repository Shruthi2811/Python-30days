
def get_dict_values(students):
    for student in students:
        name=student.get("name","Unknown")
        age=student.get("age","Unknown")
        grade=student.get("grade","Unknown")
        city=student.get("city","Unknown")
        print(f"Name: {name}, Age: {age}, Grade: {grade}, City: {city}")
    
def get_dict_values_key(students,key):
    for student in students:
        value=student.get(key,"Unknown")
        print(f"{key.capitalize()}: {value}")

students = [
    {"name": "Alice", "age": 20, "grade": "A", "city": "Seattle"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "age": 22},
    {"age": 19, "grade": "A", "city": "San Diego"},
    {"name": "Eva", "city": "Portland"}
]

get_dict_values(students)
print("\nGetting specific key values:")
get_dict_values_key(students,"name")
get_dict_values_key(students,"age")
get_dict_values_key(students,"grade")
get_dict_values_key(students,"city")

# Time complexity: O(n), where n is the number of students in the input list. This is because we iterate through the list of students once to access their values using the get() method.
# Space complexity: O(1), as we are not using any additional data structures that grow with the input size. We are simply printing the values, which does not require additional space.