#* Merge two lists into a dictionary
def merge_lists_to_dict(keys, values):
    dictionary = {}
    for key in range(len(keys)):
        dictionary[keys[key]] = values[key]
    return dictionary
# Example usage:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = merge_lists_to_dict(keys, values)
print(result)  # Output: {'a': 1, 'b': 2, 'c': 3}
# Time complexity: O(n), where n is the number of elements in the input lists. This is because we iterate through the lists once.   
# Space complexity: O(n), where n is the number of elements in the input lists. This is because we create a new dictionary to store the merged key-value pairs, and in the worst case, if all keys are unique, we will store all of them in the dictionary. Additionally, we also create a new list to store the values, which can also take up to O(n) space in the worst case.


#* Merge two lists into a dictionary using dict comprehension
def merge_lists_to_dict_comprehension(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}
# Example usage:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = merge_lists_to_dict_comprehension(keys, values)
print(result)  # Output: {'a': 1, 'b': 2, 'c': 3}
# Time complexity: O(n), where n is the number of elements in the input lists. This is because we iterate through the lists once to create the dictionary.          
# Space complexity: O(n), where n is the number of elements in the input lists. This is because we create a new dictionary to store the merged key-value pairs, and in the worst case, if all keys are unique, we will store all of them in the dictionary. Additionally, we also create a new list to store the values, which can also take up to O(n) space in the worst case.


#   * Merge two lists into a dictionary using the zip() function
def merge_lists_to_dict_zip(keys, values):
    return dict(zip(keys, values))
# Example usage:
keys = ['a', 'b', 'c']      
values = [1, 2, 3]
result = merge_lists_to_dict_zip(keys, values)
print(result)  # Output: {'a': 1, 'b': 2, 'c': 3}
# Time complexity: O(n), where n is the number of elements in the input lists. This is because we iterate through the lists once to create the dictionary using the zip() function.          
# Space complexity: O(n), where n is the number of elements in the input lists. This is because we create a new dictionary to store the merged key-value pairs, and in the worst case, if all keys are unique, we will store all of them in the dictionary. Additionally, we also create a new list to store the values, which can also take up to O(n) space in the worst case.