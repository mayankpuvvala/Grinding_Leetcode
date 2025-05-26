class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high= 0, len(nums)-1
        while low<=high:
            mid= (high-low)//2 + low
            print(mid)
            if nums[mid]==target:
                return mid
            elif nums[low] <= nums[mid] : 
                if nums[low]<= target< nums[mid]:
                    high= mid
                else:
                    low= mid+1
            else :
                if nums[mid]<target<=nums[high]:
                    low= mid+1
                else:
                    high= mid
        return -1