class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #[3,4,2] or [1,4,3,6] or [4,2]
        changed= False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if changed:
                    return False
                if i==0 or nums[i+1]>=nums[i-1]:
                    nums[i]= nums[i+1]
                else:
                    nums[i+1]= nums[i]
                changed= True
        return True

