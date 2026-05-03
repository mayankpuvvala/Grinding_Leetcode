class Solution:
    def pacificAtlantic(self, heights):
        atlantic= set()
        pacific= set()
        rows,cols= len(heights), len(heights[0])
        def dfs(i,j,visited):
            visited.add((i,j))
            for x,y in ((i,j-1),(i,j+1),(i-1,j),(i+1,j)):
                if 0<=x<rows and 0<=y<cols and heights[x][y]>=heights[i][j] and (x,y) not in visited:
                    dfs(x,y,visited)
        
        for i in range(rows):
            dfs(i,0,pacific)
            dfs(i,cols-1,atlantic)
        for j in range(cols):
            dfs(0,j,pacific)
            dfs(rows-1,j,atlantic)

        return list(pacific & atlantic)
                