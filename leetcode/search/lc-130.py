from typing import List

directions = [-1, 0, 1, 0, -1]
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


# improve code style
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


testMatrix = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
flipOtoX_betterStyle(testMatrix)
print("#### output: ", testMatrix)
