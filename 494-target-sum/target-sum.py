class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, sumi):
            if i==len(nums) and sumi==target:
                return 1
            if i>=len(nums):
                return 0
            if (i,sumi) in dp:
                return dp[(i,sumi)]
            dp[(i, sumi)] = dfs(i+1, sumi+nums[i])+ dfs(i+1, sumi-nums[i])
            return dp[(i, sumi)]
        return dfs(0, 0)