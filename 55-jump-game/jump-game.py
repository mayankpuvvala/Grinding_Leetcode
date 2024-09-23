class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas=nums[0]
        for i in range(1,len(nums)):
            if gas==0:
                return False
            gas-=1
            gas= max(gas, nums[i])
        return True
        