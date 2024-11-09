class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=j= len(nums)-1
        while j>=0:
            if nums[j]!=nums[i]:
                i=j
            elif nums[j]==nums[i] and i-j>1:
                del nums[i]
                i-=1
            j-=1
        return len(nums)



        