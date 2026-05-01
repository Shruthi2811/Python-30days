#* Find missing numbers in a sequence
def find_missing_numbers(lst):
    mini = min(lst)
    maxii = max(lst)
    missing_numbers = []
    for num in range(mini, maxii + 1):
        if num not in lst:
            missing_numbers.append(num)
    return missing_numbers
# Example usage:
input_list = [1, 2, 4, 6, 7]
result = find_missing_numbers(input_list)
print(result)  # Output: [3, 5]
# Time complexity: O(n * m), where n is the length of the input list and m is the range of numbers between the minimum and maximum values in the list. This is because we iterate through the range of numbers from the minimum to the maximum value, which takes O(m) time, and for each number in that range, we check if it is not in the input list, which takes O(n) time. Therefore, the overall time complexity is O(n * m).
# Space complexity: O(m), where m is the range of numbers between the minimum and maximum values in the list. This is because in the worst case, if all numbers in the range are missing from the input list, we will store all those missing numbers in the missing_numbers list, which can take up to O(m) space. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the missing_numbers list reference and the temporary variables used during the iteration.

def find_missing_numbers_compact(lst):
    mini = min(lst)
    maxii = max(lst)
    return [num for num in range(mini, maxii + 1) if num not in lst]
# Example usage:
input_list = [1, 2, 4, 6, 7]
result = find_missing_numbers_compact(input_list)
print(result)  # Output: [3, 5]
# Time complexity: O(n * m), where n is the length of the input list and m is the range of numbers between the minimum and maximum values in the list. This is because we iterate through the range of numbers from the minimum to the maximum value, which takes O(m) time, and for each number in that range, we check if it is not in the input list,                which takes O(n) time. Therefore, the overall time complexity is O(n * m).
# Space complexity: O(m), where m is the range of numbers between the minimum and maximum values in the list. This is because in the worst case, if all numbers in the range are missing from the input list, we will store all those missing numbers in the returned list, which can take up to O(m) space. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference and the temporary variables used during the iteration.    

