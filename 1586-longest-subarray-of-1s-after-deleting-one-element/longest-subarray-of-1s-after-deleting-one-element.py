class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        curr,prev= 0,0

        for i in nums:
            if i==1 : 
                curr+=1
            else:
                ans= max(ans, prev+curr)
                prev= curr
                curr= 0
        ans= max(ans, prev+curr)
        if ans== len(nums):
            return ans-1
        return ans