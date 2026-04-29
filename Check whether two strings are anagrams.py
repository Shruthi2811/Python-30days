#* Check whether two strings are anagrams
def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    s2 = s2.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return sorted(s1) == sorted(s2)  # Check if the sorted characters of both strings are the same
# Example usage:
string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(result)  # Output: True
# Time complexity: O(n log n), where n is the length of the input strings. This is because we sort the characters of both strings, which takes O(n log n) time, and then we compare the sorted lists, which takes O(n) time. However, the sorting step dominates the overall time complexity, resulting in O(n log n).
# Space complexity: O(n), where n is the length of the input strings. This is because we create new strings to store the modified versions of the input strings (after removing spaces and converting to lowercase), which can take up to O(n) space in the worst case if all characters are non-space characters. Additionally, we also create new lists to store the sorted characters of both strings, which can also take up to O(n) space in the worst case if all characters are unique. However, if we consider the input strings as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new string and list references.


#* Check whether two strings are anagrams using a dictionary
def are_anagrams2(s1, s2):
    s1 = s1.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    s2 = s2.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    if len(s1) != len(s2):
        return False  # If the lengths of the strings are different, they cannot be anagrams
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s2:
        if char not in char_count or char_count[char] == 0:
            return False  # If a character in s2 is not found in char_count or its count is zero, the strings are not anagrams
        char_count[char] -= 1
    return True  # If we have successfully matched all characters, the strings are anagrams
# Example usage:
string1 = "listen"
string2 = "silent"
result = are_anagrams2(string1, string2)
print(result)  # Output: True
# Time complexity: O(n), where n is the length of the input strings. This is because we iterate through both strings once: once to count the occurrences of each character in the first string, and once to check the characters in the second string against the counts in the dictionary. Both iterations take O(n) time, resulting in an overall time complexity of O(n).
# Space complexity: O(n), where n is the length of the input strings. 
# This is because in the worst case, if all characters in the strings are unique, we will store each character in the char_count dictionary, which can take up to O(n) space. Additionally, if there are duplicate characters, we will also store those characters and their counts in the dictionary, which can also take up to O(n) space in the worst case if all characters are duplicates. 
# However, if we consider the input strings as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the dictionary references.

