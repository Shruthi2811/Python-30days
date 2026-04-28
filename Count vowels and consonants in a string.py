#* Count vowels and consonants in a string
def count_vowels_consonants(s):
    vowels="aeiouAEIOU"
    vowelcnt=0
    consonant=0
    for i in s:
        if i in vowels:
            vowelcnt+=1
        elif i.isalpha():
            consonant+=1
    return vowelcnt,consonant
# Example usage:
input_string = "Hello World"
vowels, consonants = count_vowels_consonants(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")

#   Time complexity: O(n), where n is the length of the input string. This is because we iterate through each character in the string once to check if it is a vowel or a consonant.
#   Space complexity: O(1), as we are using a constant amount of space to store the count of vowels and consonants, regardless of the input string length.      

#* Count vowels and consonants in a string using collections.Counter
from collections import Counter
def count_vowels_consonants_counter(s):
    vowels="aeiouAEIOU"
    vowelcnt=0
    consonant=0
    char_count=Counter(s)
    for char, count in char_count.items():
        if char in vowels:
            vowelcnt+=count
        elif char.isalpha():
            consonant+=count
    return vowelcnt,consonant

# Example usage:
input_string = "Hello World"
vowels, consonants = count_vowels_consonants_counter(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")


#   Time complexity: O(n), where n is the length of the input string. This is because we iterate through each character in the string once to count their occurrences using the Counter class, and then we iterate through the unique characters to check if they are vowels or consonants.
#   Space complexity: O(k), where k is the number of unique characters in the input string. In the worst case, if all characters are unique, we will store all of them in the Counter object, which can take up to O(n) space in the worst case if all characters are unique. However, if we consider the input string as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the vowel and consonant count variables.

