# Number of Islands

class Solution(object):

    def dfs(self,grid,r,c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return

        grid[r][c] = "0"
        
        self.dfs(grid, r + 1, c) # Down
        self.dfs(grid, r - 1, c) # Up
        self.dfs(grid, r, c + 1) # Right
        self.dfs(grid, r, c - 1) # Left


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        island = 0
        for r in range(row):
            for c in range(column):
                if grid[r][c] == "1":
                    island += 1
                    self.dfs(grid,r,c)

        return island

        