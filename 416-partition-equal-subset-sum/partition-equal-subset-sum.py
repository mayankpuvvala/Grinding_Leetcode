class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        target = total//2
        cache= {}
        def dfs(i, sumi):
            if (i, sumi) in cache:
                return cache[(i, sumi)]
            if sumi==target:
                return True
            if i==len(nums) or sumi>target:
                return False
            cache[(i,sumi)]= dfs(i+1, sumi+nums[i]) or dfs(i+1, sumi)
            return cache[(i, sumi)]
        return dfs(0,0)