class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buy):
            if i>= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            if buy:
                res= max(dfs(i+1, False)- prices[i], dfs(i+1, True))
            else:
                res= max(dfs(i+2, True)+ prices[i] , dfs(i+1, False))
            dp[(i,buy)] = res
            return res
        return dfs(0, True)
