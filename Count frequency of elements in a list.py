#  Count frequency of elements in a list
#* Count frequency of elements in a list using a dictionary
def count_frequency(lst):
    count_frequency_dict = {}
    for item in lst:
        if item in count_frequency_dict:
            count_frequency_dict[item] += 1
        else:
            count_frequency_dict[item] = 1
    return count_frequency_dict
# Example usage:
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
result = count_frequency(my_list)
print(result)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}     
# Time complexity: O(n), where n is the number of elements in the input list. This is because we iterate through the list once to count the frequency of each element.
# Space complexity: O(k), where k is the number of unique elements in the input list. In the worst case, if all elements are unique, we will store all of them in the dictionary.   

#* Count frequency of elements in a list using collections.Counter
from collections import Counter
def count_frequency_counter(lst):
    return dict(Counter(lst))
# Example usage:
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
result = count_frequency_counter(my_list)
print(result)  # Output: {'apple': 3, 'banana': 2, 'orange': 1} 
# Time complexity: O(n), where n is the number of elements in the input list. This is because we iterate through the list once to count the frequency of each element using the Counter class.
# Space complexity: O(k), where k is the number of unique elements in the input list. In the worst case, if all elements are unique, we will store all of them in the resulting dictionary. 


