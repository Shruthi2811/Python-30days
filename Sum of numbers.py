#---------------APPROACH 1---------------------
#* Find the sum of all numbers in a list

def sum_of_numbers(lst):
    total=0
    for i in lst:
        total +=i
    return total

print(sum_of_numbers([1, 2, 3, 4, 5]))
#Time Complexity: O(n) where n is the number of elements in the list.
#Space Complexity: O(1) because we are using only a constant amount of space to store the total sum.


#---------------APPROACH 2---------------------
#* Find the sum of all numbers in a list using built-in function
def sum_of_numbers(lst):
    return sum(lst) 

print(sum_of_numbers([1, 2, 3, 4, 5]))
#Time Complexity: O(n) where n is the number of elements in the list, because the sum() function iterates through the list once.
#Space Complexity: O(1) because we are using only a constant amount of space to store the total sum.



#Find the sum of all numbers in a list - if number < 0 , sum should be 0
def sum_of_numbers(lst):
    total=0
    for i in lst:
        if i>0:
            total +=i
    return total

print(sum_of_numbers([1, 2, 3, 4, 5]))
print(sum_of_numbers([-1, -2, 3, 4, 5]))
print(sum_of_numbers([-1, -2, -3, -4, -5]))

#Time Complexity: O(n) where n is the number of elements in the list.
#Space Complexity: O(1) because we are using only a constant amount of space to store the total sum.