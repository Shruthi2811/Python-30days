def read_data_from_file(file_path,word):
    counter=0
    with open(file_path, 'r') as file:
        for line in file:
            if word in line.lower():
                counter+=1
    return counter
    

file_path = 'data.txt'  # Replace with your file path
data = read_data_from_file(file_path,"python")
print(data) 
# Time complexity: O(n*m), where n is the number of lines in the file and m is the average length of each line. This is because we read each line of the file once (O(n)) and check if the word is present in that line (O(m)).
# Space complexity: O(1), as we are using a constant amount of space to store the counter variable and temporary variables used during the file reading process. We are not storing the entire file content in memory, so the space complexity does not depend on the size of the file.
