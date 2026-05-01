#* Find the second largest number in a list
def second_largest(lst):
    if len(lst) < 2:
        return None  # Return None if there are less than 2 elements in the list
    max=0 
    secondmax=0
    for i in lst:
        if i > max and max >= secondmax:
            secondmax=max
            max=i
        if i > secondmax and i < max:
            secondmax=i
    if secondmax == float('-inf'):
        return None  # Return None if there is no second largest number (e.g., all elements are the same)
    return secondmax
# Example usage:
input_list = [7,3, 1, 4, 1, 5,    9]
result = second_largest(input_list)
print(result)  # Output: 5
# Time complexity: O(n), where n is the length of the input list. This is because we iterate through the list once to find the maximum and second maximum values, which takes O(n) time.
# Space complexity: O(1), as we are using a constant amount of space to store the maximum and second maximum values, as well as temporary variables during the iteration. We are not creating any additional data structures that grow with the input size.     
