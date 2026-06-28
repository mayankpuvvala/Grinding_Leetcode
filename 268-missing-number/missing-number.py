class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        sumi= n*(n+1)//2
        return sumi- sum(nums)
