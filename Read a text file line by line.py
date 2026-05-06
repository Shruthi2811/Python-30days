def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data
   
file_path = 'data.txt'  # Replace with your file path
data = read_data_from_file(file_path)
print(data)  # Output the contents of the file
# Time complexity: O(n), where n is the size of the file. This is because                                       we read the entire file content once, which takes O(n) time.
# Space complexity: O(n), where n is the size of the file. This is because we store the entire file content in memory as a string, which can take up to O(n) space. However, if we consider the file content as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the string reference and temporary variables used during the file reading process.