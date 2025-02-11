class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:  # Method to count the number of islands in a 2D grid
        if not grid:  # If the grid is empty, return 0
            return 0
        
        def dfs(i, j):  # Depth-First Search (DFS) to explore the island
            # Base case: If the current cell is out of bounds or not part of an island, return
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # Mark the current cell as visited by setting it to '0'
            # Recursively explore the neighboring cells (up, down, left, right)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        num_islands = 0  # Initialize the count of islands
        for i in range(len(grid)):  # Iterate through each row of the grid
            for j in range(len(grid[0])):  # Iterate through each column of the grid
                if grid[i][j] == '1':  # If the current cell is part of an unvisited island
                    num_islands += 1  # Increment the island count
                    dfs(i, j)  # Perform DFS to mark all connected cells as visited
        
        return num_islands  # Return the total number of islands
    

'''
Summary

    DSA Used: 2D Grid, Depth-First Search (DFS).

    Time Complexity: O(m * n).

    Space Complexity: O(m * n).

'''