class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols= len(grid), len(grid[0])
        self.res= 0
        visited= set()
        def dfs(r, c):
            if r<0 or r==rows or c<0 or c==cols or grid[r][c]!=1 :
                self.res+=1
                return 
            if ((r,c)) in visited:
                return
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r, c-1)
            dfs(r,c+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    break
        return self.res