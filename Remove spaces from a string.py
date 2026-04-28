#* Remove spaces from a string

def remove_spaces(s):
    for i in s:
        if i == " ":
            s=s.replace(i,"")
    return s
# Example usage:
input_string = "Hello World"
result = remove_spaces(input_string)
print(result)  # Output: "HelloWorld"

input_string2 = " Hello World. Welcome to Python programming. "
result = remove_spaces(input_string2)
print(result) # Output: "HelloWorld.WelcometoPythonprogramming."
# Time complexity: O(n), where n is the length of the input string. This is because we iterate through each character in the string once to check for spaces and replace them.
# Space complexity: O(n), where n is the length of the input string. This is because we create a new string to store the result after removing spaces, which can take up to O(n) space in the worst case if all characters are spaces. However, if we consider the input string as part of the input and not additional space, then the space complexity can be considered O(   1) since we are only using a constant amount of space for the new string reference. 


def remove_spaces2(s):
    return s.replace(" ","")
# Example usage:
input_string = "Hello World"
result = remove_spaces2(input_string)
print(result)  # Output: "HelloWorld"

input_string2 = " Hello World. Welcome to Python programming. "
result = remove_spaces2(input_string2)
print(result) # Output: "HelloWorld.WelcometoPythonprogramming."

# Time complexity: O(n), where n is the length of the input string. This is because we iterate through each character in the string once to check for spaces and replace them using the built-in replace() method.
# Space complexity: O(n), where n is the length of the input string. This is because we create a new string to store the result after removing spaces, which can take up to O(n) space in the worst case if all characters are spaces. However, if we consider the input string as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new string reference.


#* Remove spaces from a string using list comprehension
def remove_spaces3(s):
    return ''.join([char for char in s if char != ' '])
# Example usage:
input_string = "Hello World"
result = remove_spaces3(input_string)
print(result)  # Output: "HelloWorld"       
input_string2 = " Hello World. Welcome to Python programming. "
result = remove_spaces3(input_string2)
print(result) # Output: "HelloWorld.WelcometoPythonprogramming."    
# Time complexity: O(n), where n is the length of the input string. This is because we iterate through each character in the string once to check for spaces and create a new list of characters that are not spaces.
# Space complexity: O(n), where n is the length of the input string. This is because we create a new list to store the characters that are not spaces, which can take up to O(n) space in the worst case if all characters are not spaces. Additionally, we also create a new string to store the result after joining the characters, which can also take up to O(n) space in the worst case if all characters are not spaces. However, if we consider the input string as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new string reference.   


