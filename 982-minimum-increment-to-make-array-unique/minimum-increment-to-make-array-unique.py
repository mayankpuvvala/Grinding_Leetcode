class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = [0]*(len(nums)+max(nums))
        for i in nums:
            count[i]+=1
        res= 0
        for i in range(len(count)-1):
            if count[i]>1:
                diff= count[i]-1
                count[i+1]+= diff
                res+= diff
        return res