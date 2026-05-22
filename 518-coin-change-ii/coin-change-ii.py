class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, sumi):
            if sumi==amount:
                return 1
            if i==len(coins) or sumi>amount:
                return 0
            return dfs(i, sumi+coins[i]) + dfs(i+1, sumi)
        return dfs(0, 0)