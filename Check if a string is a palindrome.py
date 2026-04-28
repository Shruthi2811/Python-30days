#* Check if a string is a palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is equal to its reverse
# Example usage:
input_string = "A man a plan a canal Panama"
result = is_palindrome(input_string)
print(result)  # Output: True

# Time complexity: O(n), where n is the length of the input string. This is because we iterate through the string once to remove spaces and convert it to lowercase, and then we compare the string with its reverse, which also takes O(n) time.
# Space complexity: O(n), where n is the length of the input string. This is because we create a new string to store the modified version of the input string (after removing spaces and converting to lowercase), which can take up to O(n) space in the worst case if all characters are non-space characters. Additionally, we also create a new string to store the reverse of the modified string, which can also take up to O(n) space in the worst case if all characters are    non-space characters. However, if we consider the input string as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new string references.        


def is_palindrome2(s):
    start=0
    end=len(s)-1
    while start<end:
        while start<end and s[start]==" ":
            start+=1
        while start<end and s[end]==" ":
            end-=1
        if s[start].lower()!=s[end].lower():
            return False
        start+=1
        end-=1
    return True

        
# Example usage:
input_string = "A man a plan a canal Panama"
result = is_palindrome2(input_string)
print(result)  # Output: True      
# Time complexity: O(n), where n is the length of the input string. This is because we iterate through the string from both ends towards the center, comparing characters until we find a mismatch or reach the middle of the string.
# Space complexity: O(1), as we are using a constant amount of space to store the start and end pointers, regardless of the input string length. We are not creating any additional data structures that grow with the input size.      
