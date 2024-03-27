from typing import List

# <solution 1>
# for each cell of O:
#   bfs until reaching a level that no cell can be added to the frontier / queue

# Or:

# <solution 2>
# for all cells at the edge:
#   dfs to mark its region with Mark N (cannot be flipped)
# The mark all Os to Xs, and all Ns to Os

# passed all tests on leetcode
def flipOtoX(board: List[List[str]]) -> None:
    directions = [-1, 0, 1, 0, -1]

    def dfs(board: List[List[str]], i: int, j: int, m: int, n: int) -> None:
        if 0 <= i <= m - 1 and 0 <= j <= n - 1 and board[i][j] == 'O': # *
            # print('---- flipped at {}, {}'.format(i, j))
            board[i][j] = 'N'
        else:
            return

        for idx in range(0, 4):
            row = i + directions[idx]
            col = j + directions[idx+1]
            dfs(board, row, col, m, n)

    m, n = len(board), len(board[0])

    # empty matrix => no flip
    # 1D matrix => cannot flip
    # if any dimension <= 2 => cannot flip
    if m <= 2 or n <= 2:
        return

    # @assert m >= 3 and n >= 3

    for i in [0, m-1]: # *
        for j in range(n):
            if board[i][j] == 'O':
                dfs(board, i, j, m, n)

    for i in range(1, m-1):
        for j in [0, n-1]:
            if board[i][j] == 'O':
                dfs(board, i, j, m, n)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                # board[i][j] == 'X' # !! you make this mistake again
                board[i][j] = 'X'
            elif board[i][j] == 'N':
                board[i][j] = 'O'

    return None


# improve code style
# passed all leetcode tests
def flipOtoX_betterStyle(board: List[List[str]]) -> None:
    def dfs2(i, j):
        if not 0 <= i <= m - 1 or not 0 <= j <= n - 1 or board[i][j] != 'O':
            return
        
        board[i][j] = 'N'

        dfs2(i + 1, j)
        dfs2(i - 1, j)
        dfs2(i, j + 1)
        dfs2(i, j - 1)
    
    # empty matrix => no flip
    if not board: # *
        return
    
    # !! have to check non-empty before, otherwise will have index out of range error
    m, n = len(board), len(board[0]) 

    # 1D matrix => cannot flip
    # if any dimension <= 2 => cannot flip
    if m <= 2 or n <= 2:
        return

    # @assert m >= 3 and n >= 3

    # dfs all the border cells
    for i in range(m):
        dfs2(i, 0)
        dfs2(i, n - 1)
    for j in range(1, n - 1):
        dfs2(0, j)
        dfs2(m - 1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                # board[i][j] == 'X' # !! you make this mistake again
                board[i][j] = 'X'
            elif board[i][j] == 'N':
                board[i][j] = 'O'

# bfs approach
# 55 / 58 tests passed on leetcode, failed due to time limiet exceeded
# thus should be functionally correct
def flipOtoX_bfs(board: List[List[str]]) -> None:
    directions = [-1, 0, 1, 0, -1]

    from collections import deque
    def bfs(row, col):
        if board[row][col] != 'O':
            return
        
        # !! below is wrong, since this will be regarded as a 1d queue of len 2
        # queue = deque([row, col])
        queue = deque([[row, col]])
        while queue:
            r, c = queue.popleft() # *
            board[r][c] = "N"
            for i in range(4):
                x = r + directions[i]
                y = c + directions[i+1]
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    queue.append([x, y]) # *


    if not board:
        return
    
    m, n = len(board), len(board[0])

    if m < 3 or n < 3:
        return
    
    for i in range(m):
        bfs(i, 0)
        bfs(i, n - 1)

    for j in range(n):
        bfs(0, j)
        bfs(m - 1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "N":
                board[i][j] = "O"

# bfs approach - better code style
def flipOtoX_bfs_betterStyle(board: List[List[str]]) -> None:
    if not board:
        return
    
    m, n = len(board), len(board[0])

    if m < 3 or n < 3:
        return
    
    from collections import deque
    queue = deque()
    
    # first and last elments in each row
    for i in range(m):
        for r, c in [(i, 0), (i, n - 1)]: # *
            if board[r][c] == "O":
                queue.append((r, c))

    # first and last elments in each column
    for j in range(n):
        # for r, c in [(0, n), (i - 1, n)]: # !! easy to mix up these numbers
        for r, c in [(0, j), (m - 1, j)]: # *
            if board[r][c] == "O":
                queue.append((r, c))

    while queue:
        r, c = queue.popleft() # *
        board[r][c] = "N"
        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]: # *
            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                queue.append([x, y]) # *

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "N":
                board[i][j] = "O"


testMatrix = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
flipOtoX_bfs(testMatrix)
print("#### output: ", testMatrix)
