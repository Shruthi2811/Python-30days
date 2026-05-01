#* Flatten a list of lists
def flatten_list_of_lists(lst):
    flattened_list = []
    for sublist in lst:
        for item in sublist:
            flattened_list.append(item)
    return flattened_list
# Example usage:
input_list = [[1, 2], [3, 4], [5, 6]]
result = flatten_list_of_lists(input_list)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
# Time complexity: O(n), where n is the total number of elements in all the sublists combined. This is because we iterate through each sublist and then through each item in the sublist, which takes O(n) time in total.
# Space complexity: O(n), where n is the total number of elements in all the sublists combined. This is because we create a new list to store the flattened elements, which can take up to O(n) space in the worst case if all elements are included in the flattened list. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference and the temporary variables used during the flattening process.

def flatten_list_of_lists_compact(lst):
    return [item for sublist in lst for item in sublist]
# Example usage:
input_list = [[1, 2], [3, 4], [5, 6]]
result = flatten_list_of_lists_compact(input_list)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
# Time complexity: O(n), where n is the total number of elements in all the sublists combined. This is because we iterate through each sublist and then through each item in the sublist, which takes O(n) time in total.
# Space complexity: O(n), where n is the total number of elements in all the sublists combined. This is because we create a new list to store the flattened elements, which can take up to O(n) space in the worst case if all elements are included in the flattened list. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference and the temporary variables used during the flattening process.    

