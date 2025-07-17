class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res= 0
        visited= set()
        row, col= len(grid), len(grid[0])
        def dfs(r,c):
            if r<0 or r==row or c<0 or c==col or grid[r][c]==0:
                self.res+=1
                return
            if  (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    dfs(i,j)
                    return self.res