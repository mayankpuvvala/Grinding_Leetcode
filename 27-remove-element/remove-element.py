class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        i,j = 0,0
        while i<len(nums):
            if nums[i]!=val:
                res+=1
                nums[j]=nums[i]
                j+=1
            i+=1
        return res