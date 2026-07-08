class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two= 0, 0
        for i in range(len(nums)):
            two, one= max(two, nums[i]+one), two
        return two