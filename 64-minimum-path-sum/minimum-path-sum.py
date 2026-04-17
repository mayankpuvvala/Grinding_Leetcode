class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[0]*len(grid[0])
        dp[0]=grid[0][0]
        for i in range(1, len(grid[0])):
            dp[i]= dp[i-1]+grid[0][i]
        for i in range(1,len(grid)):
            dp[0]+= grid[i][0]
            for j in range(1, len(grid[0])):
                dp[j]=min(dp[j-1], dp[j])+grid[i][j]
        return dp[-1]
