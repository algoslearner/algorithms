'''
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

# TC : O(M * N)
# SC : O(1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        r = len(grid)
        c = len(grid[0])
        if r == None: return 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        rows = len(grid)
        col = len(grid[0])
        
        # mark visted nodes as zero
        grid[r][c] = '0'
        
        if (r - 1 >= 0 and grid[r-1][c] == '1'): self.dfs(grid, r-1, c)
        if (r + 1 < rows and grid[r+1][c] == '1'): self.dfs(grid, r+1, c)
        if (c - 1 >= 0 and grid[r][c-1] == '1'): self.dfs(grid, r, c-1)
        if (c + 1 < col and grid[r][c+1] == '1'): self.dfs(grid, r, c+1)
