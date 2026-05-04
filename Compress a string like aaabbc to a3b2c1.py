#* Compress a string like "aaabbc" to "a3b2c1"
def compress_string(s):
    if not s:
        return ""  # Return an empty string if the input string is empty
    compressed=[]
    counter=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            counter+=1
        else:
            compressed.append(s[i-1]+str(counter))
            counter=1
    compressed.append(s[-1]+str(counter))  # Append the last character and its count
    return ''.join(compressed)
# Example usage:
input_string = "aaabbc"
result = compress_string(input_string)
print(result)  # Output: "a3b2c1"
# Time complexity: O(n), where n is the length of the input string. This is because we iterate through the string once to create the compressed version, which takes O(n) time.         
# Space complexity: O(n), where n is the length of the input string. This is because in the worst case, if all characters in the string are unique, we will create a compressed string that is twice the length of the input string (each character followed by '1'), which can take up to O(n) space. However, if we consider the input string as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the compressed list reference and temporary variables used during the compression process.       

