#Merge overlapping intervals
#intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
#Two intervals overlap if the start of one interval is less than or equal to the end of another interval.
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start time
    merged = []
    for item in intervals:
        start=item[0]
        end=item[1]
        print("start:", start, "end:", end)
        print("merged:", merged )
        if merged and merged[-1][0] <= start <= merged[-1][1]:  # Check if there is an overlap with the last merged interval
                merged[-1][1] = max(merged[-1][1], end)  # Merge the intervals by updating the end time of the last merged interval
        else:
            merged.append(item)  # If there is no overlap, add the current interval to the merged list
    return merged
# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge_intervals(intervals)
print(result)  # Output: [[1, 6], [8, 10], [15, 18]]
# Time complexity: O(n log n), where n is the number of intervals in the input list. This is because we need to sort the intervals based on their start times, which takes O(n log n) time. The merging process itself takes O(n) time                      as we iterate through the sorted intervals once to merge them. Therefore, the overall time complexity is O(n log n) due to the sorting step.
# Space complexity: O(n), where n is the number of intervals in the input list. This is because in the worst case, if all intervals are non-overlapping, we will end up with a merged list that contains all the original intervals, which can take up to O(n) space. However, if we consider the input list as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the merged list reference and temporary variables used during the merging process.

