#---------------APPROACH 1---------------------
#* Filter even numbers from a list

def filter_even_numbers(lst):
    """Filter even numbers from a list.

    Args:
        lst (list): A list of integers. 
    Returns:
        list: A list containing only the even numbers from the input list.
    """
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers 
# Example usage:
numbers = [0]
even_numbers = filter_even_numbers(numbers)
print(even_numbers)  # Output: [2, 4, 6]                

# Time complexity: O(n), where n is the number of elements in the input list.   
# Space complexity: O(m), where m is the number of even numbers in the input list.

#---------------APPROACH 2---------------------
#* Filter even numbers from a list using list comprehension 
def filter_even_numbers_comprehension(lst):
    return [num for num in lst if num % 2 == 0]

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter_even_numbers_comprehension(numbers)
print(even_numbers)  # Output: [2, 4, 6]

# Time complexity: O(n), where n is the number of elements in the input list.
# Space complexity: O(m), where m is the number of even numbers in the input list.      
