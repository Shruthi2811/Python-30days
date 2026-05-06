def extract_numbers_from_file(file_path):
    numbers=[]
    with open(file_path, 'r') as file:
        for line in file:
            for sub_word in line.split():
                if sub_word.isdigit():
                    numbers.append(sub_word)
    return numbers

file_path = 'data.txt'  # Replace with your file path
data = extract_numbers_from_file(file_path)
print(data) 

# Time complexity: O(n*m), where n is the number of lines in the file and m is the average number of words in each line. This is because we read each line of the file once (O(n)) and split it into words (O(m)).      
# Space complexity: O(k), where k is the number of numeric words found in the file. This is because we store the numeric words in a list, which can grow in size depending on the number of numeric words present in the file.      

