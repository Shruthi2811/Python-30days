#---------------APPROACH 1---------------------
#* Find the max and min in a list

def find_max_min(lst):
    max=lst[0]
    min=lst[0]
    if len(lst)==0:
        return None
    for i in lst:
        if i>max:
            max=i
        elif i<min:
            min=i
    return max,min

print(find_max_min([3, 1, 4, 1, 5, 9]))
print(find_max_min([3, 1, 4, 0, 5, 9]))
print(find_max_min([3, 1, 4, -1, 5, 9]))

#Time Complexity: O(n) where n is the number of elements in the list.
#Space Complexity: O(1) because we are using only a constant amount of space to store the max and min values.   

#---------------APPROACH 2---------------------
# Find the max and min in a list using built-in functions
def find_max_min(lst):
    if len(lst)==0:
        return None
    max1=max(lst)
    min1=min(lst)
    return max1,min1


print(find_max_min([3, 1, 4, 1, 5, 9]))
print(find_max_min([3, 1, 4, 0, 5, 9]))
print(find_max_min([3, 1, 4, -1, 5, 9]))


#Time Complexity: O(n) where n is the number of elements in the list, because both max() and min() functions iterate through the list once.
#Space Complexity: O(1) because we are using only a constant amount of space to store the max and min values.

#---------------APPROACH 3---------------------
# Find the max and min in a list - if number < 0 , min/max should be 0
def find_max_min(lst):
    max=0
    min=0
    if len(lst)==0:
        return None
    for i in lst:
        if i>max:
            max=i
        elif i<min:
            min=i

    if min<0:
        min=0
    if max<0:
        max=0
    return max,min

print(find_max_min([3, 1, 4, 1, 5, 9]))
print(find_max_min([3, 1, 4, 0, 5, 9]))
print(find_max_min([3, 1, 4, -1,5, 9]))
print(find_max_min([-3, -1, -4, -1,-5, -9]))
#Time Complexity: O(n) where n is the number of elements in the list.
#Space Complexity: O(1) because we are using only a constant amount of space to store the max and min values.