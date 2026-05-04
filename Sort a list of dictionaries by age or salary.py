#Sort a list of dictionaries by age or salary
def sort_dictionaries(dict_list, key):
    return sorted(dict_list, key=lambda x: x[key])  # Sort the list of dictionaries based on the specified key (e.g., 'age' or 'salary')
# Example usage:
employees = [
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 25, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 55000}
]
sorted_by_age = sort_dictionaries(employees, "age")
print("Sorted by age:", sorted_by_age)
sorted_by_salary = sort_dictionaries(employees, "salary")
print("Sorted by salary:", sorted_by_salary)
# Time complexity: O(n log n), where n is the number of dictionaries in the input list. This is because the sorted() function uses Timsort, which has a time complexity of O(n log n) in the worst case.
# Space complexity: O(n), where n is the number of dictionaries in the input list. This is because the sorted() function creates a new list to store the sorted dictionaries, which can take up to O(n) space in the worst case if all dictionaries are unique. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference.



#   * Sort a list of dictionaries by age or salary using a custom sorting algorithm (e.g., bubble sort)
def bubble_sort_dictionaries(dict_list, key):
    n = len(dict_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if dict_list[j][key] > dict_list[j+1][key]:  # Compare the specified key values of the dictionaries
                dict_list[j], dict_list[j+1] = dict_list[j+1], dict_list[j]  # Swap if the current dictionary's key value is greater than the next dictionary's key value
    return dict_list
# Example usage:
employees = [
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 25, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 55000}
]
sorted_by_age = bubble_sort_dictionaries(employees, "age")
print("Sorted by age:", sorted_by_age)
sorted_by_salary = bubble_sort_dictionaries(employees, "salary")
print("Sorted by salary:", sorted_by_salary)                