#* Move all zeros to the end of the array 
def move_zeros(arr):
    start=0
    next=0
    while next<len(arr):
        if arr[start]==0 and arr[next]!=0:
            arr[start],arr[next]=arr[next],arr[start]
            start+=1
        if arr[start]!=0:
            start+=1
        next+=1
    return arr
# Example usage:
input_array = [0, 1, 0, 3, 12]          
result = move_zeros(input_array)
print(result)  # Output: [1, 3, 12, 0, 0]
# Time complexity: O(n), where n is the length of the input array. This is because we iterate through the array once to move all the zeros to the end, which takes O(n) time.
# Space complexity: O(1), as we are using a constant amount of space to store the start and next pointers, regardless of the input array length. We are not creating any additional data structures that grow with the input size.          

def move_zeros2(arr):
    nonzero_index=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[nonzero_index]=arr[i]
            nonzero_index+=1
    for i in range(nonzero_index,len(arr)):
        arr[i]=0
    return arr
# Example usage:
input_array = [0, 1, 0, 3, 12]
result = move_zeros2(input_array)
print(result)  # Output: [1, 3, 12, 0,      0]
# Time complexity: O(n), where n is the length of the input array. This is because we iterate through the array twice: once to move all the non-zero elements to the front and once to fill the remaining positions with zeros. Both iterations take O(n) time, resulting in an overall time complexity of O(n).
# Space complexity: O(1), as we are using a constant amount of space to store the nonzero_index pointer and temporary variables during the iteration. We are not creating any additional data structures that grow with the input size.