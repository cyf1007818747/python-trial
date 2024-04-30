from typing import List

# AC
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        # dfs: for a cell in the grid, make all the connected cells to be 0
        def dfs(row, col):
            # // if row >= m or col >= n or grid[row][col] == '0':
            if not 0 <= row < m or not 0 <= col < n or grid[row][col] == '0':
                return
            
            grid[row][col] = '0'

            for x, y in directions:
                dfs(row+x, col+y)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
