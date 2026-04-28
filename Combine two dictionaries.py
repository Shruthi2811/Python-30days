#* Combine two dictionaries
def combine_dictionaries(dict1, dict2):
    for key,val in dict2.items():
        dict1[key]=val
    print(dict1)


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = combine_dictionaries(dict1, dict2)

# Time complexity: O(n), where n is the number of key-value pairs in the second dictionary (dict2). This is because we iterate through all the items in dict2 to add them to dict1.
# Space complexity: O(1), as we are modifying dict1 in place and not using any additional data structures that grow with the input size. The space used is constant regardless of the size of the input dictionaries.

#* Combine two dictionaries using the update() method
def combine_dictionaries_update(dict1, dict2):
    dict1.update(dict2)
    print(dict1)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = combine_dictionaries_update(dict1, dict2)

# Time complexity: O(n), where n is the number of key-value pairs in the second dictionary (dict2). This is because the update() method iterates through all the items in dict2 to add them to dict1.
# Space complexity: O(1), as we are modifying dict1 in place and not using any additional data structures that grow with the input size. The space used is constant regardless of the size of the input dictionaries.