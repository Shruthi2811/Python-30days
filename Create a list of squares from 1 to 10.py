#* Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Time complexity: O(n), where n is the number of elements in the range (in this case, 10).
# Space complexity: O(n), where n is the number of elements in the resulting list of squares (in this case, 10). 

#* Create a list of squares from 1 to 10 using a for loop
squares = []
for x in range(1, 11):
    squares.append(x**2)
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]            

# Time complexity: O(n), where n is the number of elements in the range (in this case, 10).
# Space complexity: O(n), where n is the number of elements in the resulting list of squares (in this case, 10).

