#* Find all pairs with a target sum
#numbers = [2, 4, 3, 5, 7, 8, 9]
#target = 7
def find_pairs_with_target_sum(lst, target_sum):
    pairs = []
    for i in range(len(lst)):
        if lst[i] < target_sum and target_sum - lst[i] in lst[i+1:]:  # Only consider numbers less than the target sum
            pairs.append((lst[i], target_sum - lst[i]))
    return pairs

# Example usage:            
numbers = [2, 4, 3, 5, 7, 8, 9]         
target = 7
result = find_pairs_with_target_sum(numbers, target)
print(result)  # Output: [(2, 5), (4, 3)]
# Time complexity: O(n^2), where n is the length of the input list. This is because for each element in the list, we check if the complement (target_sum - current element) exists in the remaining part of the list, which takes O(n) time. Therefore, the overall time complexity is O(n^2).
# Space complexity: O(p), where p is               the number of pairs found that sum up to the target. This is because we store the pairs in a list, and in the worst case, if all elements in the list can form pairs that sum up to the target, we could have O(n/2) pairs, which simplifies to O(n) space complexity. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the pairs list reference and the temporary variables used during the iteration. 
