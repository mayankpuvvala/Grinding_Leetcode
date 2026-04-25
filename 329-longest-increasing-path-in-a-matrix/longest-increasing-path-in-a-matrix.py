class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j, val):
            if i<0 or j<0 or i==rows or j==cols:
                return 0
            if val>=matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res= 1+max(
                dfs(i+1, j, matrix[i][j]),  
                dfs(i, j+1, matrix[i][j]),  
                dfs(i-1, j, matrix[i][j]), 
                dfs(i, j-1, matrix[i][j]) 
            )
            dp[(i,j)] = res
            return res
        return max(dfs(i,j, float('-inf')) for i in range(rows) for j in range(cols))