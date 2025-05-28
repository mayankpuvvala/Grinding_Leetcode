class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x, y = 0, len(nums)
        for i in range(len(nums)):
            if nums[i]<x or nums[i]>y:
                nums[i]=0

        for i in range(len(nums)):
            curr = abs(nums[i])
            if x< curr <=y:
                if nums[curr-1]>0:
                    nums[curr-1]*=-1
                elif nums[curr-1]==0:
                    nums[curr-1]  = -(len(nums)+1) #not necessary as this check is done at the last return statement

        n=1
        for i in nums:
            if i>=0:
                return n
            n+=1
        return len(nums)+1