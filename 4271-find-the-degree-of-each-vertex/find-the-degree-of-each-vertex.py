class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res=[]
        for i in range(len(matrix)):
            count=0
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    count+=1
            res.append(count)
        return res