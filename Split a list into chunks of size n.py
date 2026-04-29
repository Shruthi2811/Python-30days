#* Split a list into chunks of size n 
def split_list_into_chunks(lst, n):
    newlist=[]
    for i in range(0, len(lst), n):
        sublst=lst[i:i+n]
        newlist.append(sublst)
    return newlist
# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
result = split_list_into_chunks(input_list, chunk_size)
print(result)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Time complexity: O(n), where n is the length of the input list. This is because we iterate through the list once to create the chunks, which takes O(n) time.
# Space complexity: O(n), where n is the length of the input list. This is because in the worst case, if the chunk size is 1, we will create a new list that contains all the elements of the input list, which can take up to O(n) space. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference and the temporary variables used during the chunking process.

def split_list_into_chunks_compact(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
result = split_list_into_chunks(input_list, chunk_size)
print(result)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Time complexity: O(n), where n is the length of the input list. This is because we iterate through the list once to create the chunks, which takes O(n) time.
# Space complexity: O(n), where n is the length of the input list. This is because in the worst case, if the chunk size is 1, we will create a new list that contains all the elements of the input list, which can take up to O(n) space. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new list reference and the temporary variables used during the chunking process.

