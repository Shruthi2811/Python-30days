#* Find the longest word in a sentence
def find_longest_word(sentence):
    splitwords = sentence.split()
    maxlen=0
    print(splitwords)
    for word in splitwords:
        maxlen = max(maxlen, len(word))
        if len(word) == maxlen:
            longestword=word
    return longestword
# Example usage:


result = find_longest_word("I love solving coding problems")
print(result)

# Time complexity: O(n), where n is the number of words in the sentence. This is because we iterate through the list of words once to find the longest word, which takes O(n) time.
# Space complexity: O(1), as we are using a constant amount of space to store the longest word and temporary variables during the iteration. We are not creating any additional data structures that grow with the input size.

def find_longest_word_compact(sentence):
    splitwords = sentence.split()
    longestword = max(splitwords, key=len)
    return longestword
# Example usage:
result = find_longest_word_compact("I love solving coding problems")
print(result)
# Time complexity: O(n), where n is the number of words in the sentence. This is because we iterate through the list of words once to find the longest word using the max function, which takes O(n) time.
# Space complexity: O(1), as we are using a constant amount of space to store the longest word and temporary variables during the iteration. We are not creating any additional data structures that grow with the input size.  
