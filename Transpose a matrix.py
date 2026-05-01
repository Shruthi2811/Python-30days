#* Transpose a matrix
#* Given a 2D integer array matrix, return the transpose of matrix.
matrix = [
    [7, 8],
    [9, 10],
    [11, 12]
]
def transpose(matrix):
    mat1=[]
    mat2=[]
    for i in range(len(matrix)):
        mat1.append(matrix[i][0])
        mat2.append(matrix[i][1])
    return [mat1, mat2]
# Example usage:
result = transpose(matrix)
print(result)  # Output: [[7, 9, 11], [8, 10, 12]]
# Time complexity: O(m*n), where m is the number of rows and n is the number of columns in the input matrix. This is because we iterate through each element of the matrix once to create the transposed matrix, which takes O(m*n) time.
# Space complexity: O(m*n), where m is the number of rows and n is the number of columns in the input matrix. This is because we create a new matrix to store the transposed values, which can take up to O(m*n) space in the worst case. However, if we consider the input matrix as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new matrix reference and temporary variables during the transposition process.        


def transpose_compact(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
# Example usage:
result = transpose_compact(matrix)
print(result)  # Output: [[7, 9, 11], [8, 10, 12]]
# Time complexity: O(m*n), where m is the number of rows and n is the number of columns in the input matrix. This is because we iterate through each element of the matrix once to create the transposed matrix, which takes O(m*n) time.
# Space complexity: O(m*n), where m is the number of rows and n is the                      number of columns in the input matrix. This is because we create a new matrix to store the transposed values, which can take up to O(m*n) space in the worst case. However, if we consider the input matrix as part of the input and not additional space, then the space complexity can be considered O(1) since we are only using a constant amount of space for the new matrix reference and temporary variables during the transposition process.       

