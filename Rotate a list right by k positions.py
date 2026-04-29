#* Rotate a list right by k positions
def rotate_list_right(lst, k):
    counter = 0
    while counter < k:
        lastitem = lst[-1]  # Get the last item of the list
        for i in range(len(lst)-1, 0, -1):
            lst[i] = lst[i-1]  # Shift each item to the right
        lst[0] = lastitem  # Place the last item at the beginning of the list
        counter += 1
    return lst
# Example usage:
input_list = [1, 2, 3, 4, 5]
k = 8
result = rotate_list_right(input_list, k)           
print(result)  # Output: [4, 5, 1, 2, 3]
# Time complexity: O(n * k), where n is the length of the input list and k is the number of positions to rotate. This is because we have a while loop that runs k times, and within each iteration of the while loop, we have a for loop that iterates through the list, which takes O(n) time. Therefore, the overall time complexity is O(n * k).
# Space complexity: O(1), as we are rotating the list in place and not using any additional data structures that grow with the input size. We are only using a constant amount of space for temporary variables during the rotation process.        

def rotate_list_right_compact(lst, k):
    k = k % len(lst)  # Handle cases where k is greater than the length of the list
    return lst[-k:] + lst[:-k]  # Rotate the list by slicing and concatenating
# Example usage:
input_list = [1, 2, 3, 4, 5]
k = 8
result = rotate_list_right_compact(input_list, k)
print(result)  # Output: [4, 5, 1, 2, 3]
# Time complexity: O(n), where n is the length of the input list. This is because slicing the list takes O(n) time, and concatenating the two slices also takes O(n) time, resulting in an overall time complexity of O(n).
# Space complexity: O(n), where n is the length of the input list. This is because slicing the list creates new lists for the two slices, which can take up to O(n) space in the worst case if all elements are included in one of the slices. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference and the temporary variable used to store the value of k.    