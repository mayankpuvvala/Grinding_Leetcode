class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high= 0, len(nums)-1
        while low<high:
            mid= (low+high)//2
            if nums[mid]== target:
                return mid
            elif nums[mid]<target:
                low= mid+1
            else:
                high= mid
        if target<nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        return low