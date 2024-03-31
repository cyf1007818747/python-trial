from typing import List

# (finish in half hour with tiny hint from official solution)
# passed all leetcode cases
directions = [0, 1, 0, -1, 0]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, cur) -> bool:
            # you must check this index range first before any other check 
            # to prevent index out of range error # *
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])):
                return False

            if board[i][j] == '1' or cur >= len(word):
                return False
        
            if cur == len(word) - 1:
                if word[cur] == board[i][j]:
                    return True
                else:
                    return False

            if word[cur] != board[i][j]:
                return False
                
            temp = board[i][j]
            board[i][j] = '1'
            
            for d in range(4):
                if dfs(i+directions[d], j+directions[d+1], cur+1):
                    board[i][j] = temp
                    return True
                
            board[i][j] = temp
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
                    
        return False