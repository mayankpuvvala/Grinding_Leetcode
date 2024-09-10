class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=sum(nums)
        for i,element in enumerate(nums):
            rightsum-= element
            if leftsum==rightsum:
                return i
            leftsum+= element

        return -1
