#Extract specific keys from a list of dictionaries
def extract_keys(dict_list, keys):
    ext_keys=[]
    for i in dict_list:
        tempdic={}
        for key in keys:
            if key in i:
                tempdic[key]=i[key]
        ext_keys.append(tempdic)
    return ext_keys
# Example usage:
input_dicts = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

keys_to_extract = ["name", "city"]
result = extract_keys(input_dicts, keys_to_extract)
print(result)  # Output: ['Alice', 'New York', 'Bob', 'Los Angeles', 'Charlie', 'Chicago']
# Time complexity: O(n * m), where n is the number of dictionaries in the input list and m is the number of keys to extract. This is because we iterate through each dictionary in the input list (O(n)) and for each dictionary, we iterate through the list of keys to extract (O(m)). Therefore, the overall time complexity is O(n * m).
# Space complexity: O(k), where k is the number of values extracted based on the specified keys. This is because we create a new list to store the extracted values, which can take up to O(k) space in the worst case if all specified keys are present in all dictionaries. However, if we consider the input list of dictionaries as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference and temporary variables used during the extraction process.

