class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1==word2:
            return 0
        m, n = len(word1), len(word2) 
        if not word1 or not word2:
            return m or n
        
        dp = [[0]*(n +1) for _ in range(m +1)]

        for j in range(n+1):
            dp[m][j] = n - j
        
        for i in range(m+1):
            dp[i][n] = m - i
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i]==word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1+ min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1]) #insert, delete, replace
        return dp[0][0]