class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n= len(nums)
        if n==0:    return None
        if n==1:    return 0
        if nums[0]>nums[1]:    return 0
        if nums[n-1]>nums[n-2]:     return n-1
        i,j=0,n-1
        while i<=j:
            mid= i+(j-i)//2
            if (mid==0 or nums[mid]>nums[mid-1]) and (mid==n-1 or nums[mid]>nums[mid+1]):
                return mid
            elif mid>0 and nums[mid]<nums[mid-1]:
                j=mid-1
            else:
                i=mid+1
        return None