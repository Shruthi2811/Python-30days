#* Remove duplicates from a list while preserving order
def remove_duplicates(lst):
    seen = set()
    unique_lst = []
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst   
# Example usage:
my_list = [1, 2, 3, 2, 4, 1, 5]
result = remove_duplicates(my_list)
print(result)  # Output: [1, 2, 3, 4, 5]    

# Time complexity: O(n), where n is the number of elements in the input list. This is because we iterate through the list once.
# Space complexity: O(n), where n is the number of unique elements in the input list. In the worst case, if all elements are unique, we will store all of them in the `seen` set and the `unique_lst`.

##* Remove duplicates in-place from a list while preserving order
def remove_duplicates_in_place(lst):
    seen = set()
    write_index = 0
    for read_index in range(len(lst)):
        if lst[read_index] not in seen:
            seen.add(lst[read_index])
            lst[write_index] = lst[read_index]
            write_index += 1
    return lst[:write_index]
# Example usage:
my_list = [1, 2, 3, 2, 4, 1, 5]
result = remove_duplicates_in_place(my_list)
print(result)  # Output: [1, 2, 3, 4, 5]

# Time complexity: O(n), where n is the number of elements in the input list. This is because we iterate through the list once.         
# Space complexity: O(n), where n is the number of unique elements in the input list. In the worst case, if all elements are unique, we will store all of them in the `seen` set. However, we are modifying the list in-place, so we do not use additional space for another list to store unique elements.

#   * Remove duplicates from a list while preserving order using dict.fromkeys()
def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))
# Example usage:
my_list = [1, 2, 3, 2, 4, 1, 5]
result = remove_duplicates_dict(my_list)
print(result)  # Output: [1, 2, 3, 4, 5]

# Time complexity: O(n), where n is the number of elements in the input list. This is because we iterate through the list once to create the dictionary.
# Space complexity: O(n), where n is the number of unique elements in the input list. In the worst case, if all elements are unique, we will store all of them in the dictionary. However, we are creating a new list to store the unique elements, so we also have
# space complexity of O(n) for the resulting list.
            