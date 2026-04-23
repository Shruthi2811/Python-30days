#* Find common elements between two lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))
# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_common_elements(list1, list2)
print(result)  # Output: [4, 5]

# Time complexity: O(n + m), where n and m are the lengths of the two lists.
# Space complexity: O(n + m), where n and m are the lengths of the two lists.

#* Find common elements between two lists using list comprehension
def find_common_elements_comprehension(list1, list2):
    return [element for element in list1 if element in list2]
# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_common_elements_comprehension(list1, list2)
print(result)  # Output: [4, 5]

# Time complexity: O(n * m), where n and m are the lengths of the two lists. This is because for each element in list1, we check if it exists in list2.
# Space complexity: O(k), where k is the number of common elements between the two lists. In the worst case, if all elements are common, we will store all of them in the resulting list.   


#* Find common elements between two lists using set intersection
def find_common_elements_set(list1, list2):
    return list(set(list1).intersection(set(list2)))
# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]     

result = find_common_elements_set(list1, list2)
print(result)  # Output: [4, 5] 

# Time complexity: O(n + m), where n and m are the lengths of the two lists. This is because we convert both lists to sets, which takes O(n) and O(m) time respectively, and then we perform the intersection operation, which takes O(min(n, m)) time.     
# Space complexity: O(n + m), where n and m are the lengths of the two lists. This is because we create two sets to store the unique elements of each list, and in the worst case, if all elements are unique, we will store all of them in the sets. Additionally, we create a new list to store the common elements, which can also take up to O(min(n, m)) space in the worst case.