#* Count word frequency in a sentence
def count_word_frequency(sentence):
    word_frequency={}
    for word in sentence.split():
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] = word_frequency.get(word) + 1
    return word_frequency   
# Example usage:        
result = count_word_frequency("hello world hello")
print(result)  # Output: {'hello': 2, 'world': 1}
# Time complexity: O(n), where n is the number of words in the sentence. This is because we iterate through the list of words once to count the frequency of each word, which takes O(n) time.
# Space complexity: O(m), where m is the number of unique words in the sentence. This is because we store the frequency of each unique word in the word_frequency dictionary, which can take up to O(m) space in the worst case if all words in the sentence are unique. However, if we consider the input sentence as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount       of space for the dictionary reference and the temporary variables used during the counting process.     

def count_word_frequency_compact(sentence):
    word_frequency={}
    for word in sentence.split():
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency
# Example usage:        
result = count_word_frequency_compact("hello world hello")
print(result)  # Output: {'hello': 2, 'world': 1}
# Time complexity: O(n), where n is the number of words in the sentence. This is because we iterate through the list of words once to count the frequency of each word, which takes O(n) time.
# Space complexity: O(m), where m is the number of unique words in the sentence. This is because we store the frequency of each unique word in the word_frequency dictionary, which can take up to O(m) space in the worst case if all words in the sentence are unique. However, if we consider the input sentence as part of the input and not additional space           , then the space complexity can be considered O(1) since we are only using a constant amount of space for the dictionary reference and the temporary variables used during the counting process.    
