class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(sumi):
            #if (sumi) in memo: return memo[sumi] and below before return memo[sumi]=ways
            if sumi==target:
                return 1
            if sumi>target:
                return 0
            ways= 0
            for num in nums:
                ways+= dfs(sumi+num)
            return ways
        return dfs(0)