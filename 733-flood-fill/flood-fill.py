class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        self.color = color
        row, col = len(image), len(image[0])
        def dfs(i,j, val):
            if i<0 or i==row or j<0 or j==col or image[i][j]!= val:
                return 
            image[i][j]= self.color
            dfs(i+1,j, val)
            dfs(i, j+1, val)
            dfs(i-1, j, val)
            dfs(i, j-1, val)

        dfs(sr, sc, image[sr][sc])
        return image