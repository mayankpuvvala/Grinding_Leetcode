class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i,j):
            if i>=m or j>=n or obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            return dfs(i+1, j) + dfs(i,j+1)
        return dfs(0,0)