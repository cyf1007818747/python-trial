# All copied from ChatGPT

"""
LeetCode Problem 348, "Design Tic-Tac-Toe", asks you to design a Tic-Tac-Toe game that can be played on 
an n x n grid. You will implement the TicTacToe class:

TicTacToe(int n) initializes the object the size of the board n.
int move(int row, int col, int player) represents making a move by the player (player = 1 or 2) on the 
board at position (row, col). The move is guaranteed to be valid and is placed on an empty block. 
After the move is made, return:
0 if no one wins.
1 if player 1 wins.
2 if player 2 wins.
3 if all the positions on the board are filled but no one wins (This condition is actually not 
directly mentioned in the problem but is a common edge case to consider).

A straightforward approach to designing this game is to maintain a 2D array representing the board. 
However, to efficiently check for a win after each move, we can use an array to keep track of the 
number of moves for each player in each row, column, and the two diagonals. A player wins if one 
of the counts reaches n (the size of the board).
"""

class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # Determine the player's move value
        move_val = 1 if player == 1 else -1
        
        # Update the row, column, and possibly the diagonals
        self.rows[row] += move_val
        self.cols[col] += move_val
        
        # Check diagonal
        if row == col:
            self.diagonal += move_val
        
        # Check anti-diagonal
        if col == self.size - row - 1:
            self.anti_diagonal += move_val
        
        # Check if this move wins the game
        # this is how you spit lines # *
        if abs(self.rows[row]) == self.size or \
           abs(self.cols[col]) == self.size or \
           abs(self.diagonal) == self.size or \
           abs(self.anti_diagonal) == self.size:
            return player
        
        # No winner yet
        return 0

# Example of usage
tic_tac_toe = TicTacToe(3)
print(tic_tac_toe.move(0, 0, 1))  # Output: 0
print(tic_tac_toe.move(0, 2, 2))  # Output: 0
print(tic_tac_toe.move(2, 2, 1))  # Output: 0
print(tic_tac_toe.move(1, 1, 2))  # Output: 0
print(tic_tac_toe.move(2, 0, 1))  # Output: 0
print(tic_tac_toe.move(1, 0, 2))  # Output: 0
print(tic_tac_toe.move(2, 1, 1))  # Output: 1 (Player 1 wins)
