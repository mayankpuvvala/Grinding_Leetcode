class Solution:
    def jump(self, nums: List[int]) -> int:
        res= 0
        l,r= 0,0
        while r<len(nums)-1:
            r, l= max(i+nums[i] for i in range(l,r+1)), r+1
            res+=1
        return res
