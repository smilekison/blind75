def exist(self, board, word):  # Method to check if the word exists in the board
    if not board:  # If the board is empty, return False
        return False
    for i in range(len(board)):  # Iterate through each row of the board
        for j in range(len(board[0])):  # Iterate through each column of the board
            if self.dfs(board, i, j, word):  # Perform DFS to check if the word can be formed starting at (i, j)
                return True  # If the word is found, return True
    return False  # If the word is not found after checking all positions, return False

# Check whether the word can be formed starting at (i, j) position
def dfs(self, board, i, j, word):
    if len(word) == 0:  # If all characters of the word are checked, return True
        return True
    # If the current position is out of bounds or the current character does not match, return False
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    tmp = board[i][j]  # Store the current character temporarily
    board[i][j] = "#"  # Mark the current cell as visited to avoid reuse
    # Recursively check the neighboring cells (up, down, left, right) for the remaining part of the word
    res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
          or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
    board[i][j] = tmp  # Restore the original character after DFS
    return res  # Return the result of the DFS


'''
Summary

    DSA Used: 2D Grid, Depth-First Search (DFS), Backtracking.

    Time Complexity: O(m * n * 4^L).

    Space Complexity: O(L).

'''