#* Find duplicate characters in a string
def find_duplicate_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] > 1:
            print({char : char_count[char]})  # Return a dictionary with the duplicate character and its count


# Example usage:
input_string = "programming"
result = find_duplicate_characters(input_string)
# Output: {'r': 2}, {'o': 2}, {'g': 2}, {'m': 2}
# Time complexity: O(n), where n is the length of the input string. This is because we iterate through the string once to count the occurrences of each character, which takes O(n) time, and then we iterate through the string again to find the duplicate characters, which also takes O(n) time, resulting in an overall time complexity of O(n).
# Space complexity: O(n), where n is the length of the input string. This is because in the worst case, if all characters in the string are unique, we will store each character in the char_count dictionary, which can take up to O(n) space. Additionally, if there are duplicate characters, we will also store those characters and their counts in the dictionary, which can also take up to O(n) space in the worst case if all characters are duplicates. However, if we consider the input string as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the dictionary references.
# 
# 
# * Find duplicate characters in a string using a set  
def find_duplicate_characters2(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    for char in duplicates:
        print({char : s.count(char)})  # Return a dictionary with the duplicate character and its count
# Example usage:
input_string = "programming"
result = find_duplicate_characters2(input_string)
# Output: {'r': 2}, {'o': 2}, {'g': 2}, {'m': 2}
# Time complexity: O(n^2), where n is the length of the input string. This is because we iterate through the string once to check for duplicates, which takes O(n) time, and then for each duplicate character, we count its occurrences using the count() method, which itself iterates through the string, resulting in a nested loop effect.
# Space complexity: O(n), where n is the length of the input string. This is because in the worst case, if all characters in the string are unique, we will store each character        