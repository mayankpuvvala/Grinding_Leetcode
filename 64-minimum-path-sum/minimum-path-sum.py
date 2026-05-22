class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        @cache
        def dfs(i,j):
            if i>=row or j>=col:
                return float("inf")
            if i==row-1 and j==col-1:
                return grid[i][j]

            return grid[i][j] + min(dfs(i+1,j), dfs(i,j+1))
        return dfs(0,0)