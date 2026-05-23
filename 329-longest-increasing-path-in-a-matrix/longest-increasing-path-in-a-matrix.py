class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        @cache
        def dfs(i,j, prev):
            if i<0 or j<0 or i>=rows or j>=cols or  matrix[i][j]<=prev: 
                return 0
            prev= matrix[i][j]
            return 1+ max(
            dfs(i+1, j, prev),
            dfs(i-1, j, prev),
            dfs(i, j-1, prev),
            dfs(i, j+1, prev) )
        ans= 0
        for i in range(rows):
            for j in range(cols):
                ans= max(ans, dfs(i,j, float("-inf")))
        return ans