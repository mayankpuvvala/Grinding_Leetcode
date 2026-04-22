class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, sumi):
            if sumi== amount:
                return 1
            if i>= len(coins) or sumi>amount:
                return 0
            if (i,sumi) in dp:
                return dp[(i, sumi)]
            dp[(i, sumi)] = dfs(i, sumi+coins[i])+ dfs(i+1, sumi)
            return dp[(i,sumi)]
        return dfs(0,0)