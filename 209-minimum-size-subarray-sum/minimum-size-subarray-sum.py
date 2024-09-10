class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res= len(nums)+1
        l,r=0,0
        sum=0
        while r<len(nums):
            sum+=nums[r]
            while sum>=target:
                res= min(res, r-l+1)
                sum-=nums[l]
                l+=1
            r+=1
        if res== len(nums)+1:
            return 0
        return res