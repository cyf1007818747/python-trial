from typing import List

# solution of space optimization
# passed all leetcode tests and has very good performance (due to space optimization)
def maximalSquare(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])

    # given m , n >= 1
    if m <= 1 or n <= 1:
        return 0 + any('1' in row for row in matrix) # *
    
    prev_row = [0] * n
    curr_row = [0] * n
    max_side = 0
    for i in range(n):
        prev_row[i] = 0 + (matrix[0][i] == '1')
        max_side = max(max_side, prev_row[i])
    
    # print("prev_row: ", prev_row)
    
    for i in range(1, m):
        curr_row[0] = 0 + (matrix[i][0] == '1')
        max_side = max(max_side, curr_row[0])
        for j in range(1, n):
            curr_row[j] = min(curr_row[j - 1], prev_row[j], prev_row[j - 1]) + 1 if matrix[i][j] == '1' else 0
            max_side = max(max_side, curr_row[j])
        prev_row = curr_row.copy()
        # print("prev_row: ", prev_row)
    
    return max_side ** 2

testMatrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] # expect: 4
testMatrix2 = [["0","1"],["1","0"]] # expect: 1
testMatrix3 = [
    ["1","0","1","1","0","1"],
    ["1","1","1","1","1","1"],
    ["0","1","1","0","1","1"],
    ["1","1","1","0","1","0"],
    ["0","1","1","1","1","1"],
    ["1","1","0","1","1","1"]
] # expect: 4

output = maximalSquare(testMatrix)
print("#### output: ", output)



    




    
