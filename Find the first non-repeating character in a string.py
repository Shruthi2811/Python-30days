#* Find the first non-repeating character in a string
def first_non_repeating_character(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None  # Return None if there is no non-repeating character   
# Example usage:
input_string = "swiss"
result = first_non_repeating_character(input_string)
print(result)  # Output: "w"
# Time complexity: O(n^2), where n is the length of the input string. This is because for each character in the string, we are counting its occurrences using the count() method, which itself iterates through the string, resulting in a nested loop effect.
# Space complexity: O(1), as we are using a constant amount of space to store the character being checked and the return value. We are not creating any additional data structures that grow with the input size.   
def first_non_repeating_character2(s):
    for i in range(len(s)):
        if s[i] not in s[:i] and s[i] not in s[i+1:]:
            return s[i]
    return None  # Return None if there is no non-repeating character
# Example usage:
input_string = "swiss"
result = first_non_repeating_character2(input_string)
print(result)  # Output: "w"
# Time complexity: O(n^2), where n is the length of the input string. This is because for each character in the string, we are checking if it is present in the substrings before and after it, which involves iterating through those substrings, resulting in a nested loop effect.
# Space complexity: O(1), as we are using a constant amount of space to store the index and the return value. We are not creating any additional data structures that grow with the input size.     


#* Find the first non-repeating character in a string using a dictionary
def first_non_repeating_character3(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None  # Return None if there is no non-repeating character
# Example usage:
input_string = "swiss"
result = first_non_repeating_character3(input_string)
print(result)  # Output: "w"
# Time complexity: O(n), where n is the length of the input string. This is because we iterate through the string twice: once to count the occurrences of each character and once to find the first non-repeating character. Both iterations take O(n) time, resulting in an overall time complexity of O(n).
# Space complexity: O(n), where n is the length of the input string. This is because in the worst case, if all characters in the string are unique, we