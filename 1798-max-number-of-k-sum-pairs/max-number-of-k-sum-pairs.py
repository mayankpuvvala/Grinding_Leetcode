class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i,j=0,len(nums)-1
        count=0
        nums= sorted(nums)
        while i<j:
            if (nums[j]+nums[i] ) ==k:
                count+=1
                i+=1
                j-=1
            elif (nums[i]+nums[j])>k:
                j-=1
            else:
                i+=1
        
        return count