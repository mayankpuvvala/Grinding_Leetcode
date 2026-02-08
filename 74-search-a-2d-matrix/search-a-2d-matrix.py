class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])
        low, high = 0, rows -1 
        j= cols-1
        while low<= high:
            mid = low + (high -low)//2
            if target > matrix[mid][-1]:
                low = mid+1
            elif target < matrix[mid][0]:
                high = mid-1
            else:
                break
        else:
            return False
        i= mid
        low , high = 0, cols-1
        while low<= high:
            mid = low+ (high - low)//2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                high = mid-1
            else:
                low = mid +1
        return False