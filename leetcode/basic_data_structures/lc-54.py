from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0

        ans.append(matrix[i][j])
        matrix[i][j] = 111

        while True:
            initial_i, initial_j = i, j

            while j + 1 < n and matrix[i][j+1] != 111:
                j += 1
                ans.append(matrix[i][j])
                matrix[i][j] = 111

            while i + 1 < m and matrix[i+1][j] != 111:
                i += 1
                ans.append(matrix[i][j])
                matrix[i][j] = 111

            while j - 1 >= 0 and matrix[i][j-1] != 111:
                j -= 1
                ans.append(matrix[i][j])
                matrix[i][j] = 111

            while i - 1 >= 0 and matrix[i-1][j] != 111:
                i -= 1
                ans.append(matrix[i][j])
                matrix[i][j] = 111

            if i == initial_i and j == initial_j:
                break

        return ans
 