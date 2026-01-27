class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        res= 0
        for i in prices:
            mini= min(mini, i)
            res= max(res, i-mini)
        return res