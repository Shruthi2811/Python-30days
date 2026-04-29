#Sort a list of tuples by the second element

def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])  # Sort the list of tuples based on the second element (index 1) 
# Example usage:
input_tuples = [(1, 3), (2, 1), (3, 2)]
result = sort_tuples(input_tuples)
print(result)  # Output: [(2, 1), (3, 2), (1, 3)]
# Time complexity: O(n log n), where n is the number of tuples in the input list. This is because the sorted() function uses Timsort, which has a time complexity of O(n log n) in the worst case.
# Space complexity: O(n), where n is the number of tuples in the input list. This is because the sorted() function creates a new list to store the sorted tuples, which can take up to O(n) space in the worst case if all tuples are unique. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference.


#* Sort a list of tuples by the second element using a custom sorting algorithm (e.g., bubble sort)
def bubble_sort_tuples(tuples_list):
    n = len(tuples_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if tuples_list[j][1] > tuples_list[j+1][1]:  # Compare the second elements of the tuples
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]  # Swap if the current tuple's second element is greater than the next tuple's second element
    return tuples_list
# Example usage:
input_tuples = [(1, 3), (2, 1), (3, 2)]
result = bubble_sort_tuples(input_tuples)
print(result)  # Output: [(2, 1), (3, 2), (1, 3)]
# Time complexity: O(n^2), where n is the number of tuples in the input list. This is because the bubble sort algorithm has a time complexity of O(n^2) in the worst case, as it requires nested loops to compare and swap elements.                
# Space complexity: O(1), as we are sorting the list in place and not using any additional data structures that grow with the input size. We are only using a constant amount of space for temporary variables during the swapping process.     
        