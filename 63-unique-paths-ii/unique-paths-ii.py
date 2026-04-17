class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        dp= [0]*len(obstacleGrid[0])
        dp[0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                    continue
                elif j>0:
                    dp[j]+=dp[j-1]
        return dp[-1]