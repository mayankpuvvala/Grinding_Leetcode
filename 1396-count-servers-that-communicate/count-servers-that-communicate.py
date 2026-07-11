class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        rows = [0]*row
        cols = [0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    rows[i]+=1
                    cols[j]+=1
        
        res= 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (rows[i]>1 or cols[j]>1):
                    res+=1
        return res
