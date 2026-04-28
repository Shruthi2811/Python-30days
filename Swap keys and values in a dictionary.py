#* Swap keys and values in a dictionary

def swap_dict_keys_values(d):
    swapdict={}
    for key,val in d.items():
        print(key,val)
        swapdict[val]=key
    return swapdict

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = swap_dict_keys_values(my_dict)
print(result)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Time complexity: O(n), where n is the number of key-value pairs in the input dictionary. This is because we iterate through all the items in the dictionary to create the swapped dictionary.
# Space complexity: O(n), where n is the number of key-value pairs in the input dictionary. This is because we create a new dictionary to store the swapped key-value pairs, and in the worst case, if all keys and values are unique, we will store all of them in the new dictionary.



def swap_dict_keys_values_upd(d):
    return{val:key for key,val in d.items()}

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = swap_dict_keys_values_upd(my_dict)
print(result)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Time complexity: O(n), where n is the number of key-value pairs in the input dictionary. This is because we iterate through all the items in the dictionary to create the swapped dictionary using dictionary comprehension.
# Space complexity: O(n), where n is the number of key-value pairs in the input dictionary. This is because we create a new dictionary to store the swapped key-value pairs, and in the worst case, if all keys and values are unique, we will store all of them in the new dictionary.