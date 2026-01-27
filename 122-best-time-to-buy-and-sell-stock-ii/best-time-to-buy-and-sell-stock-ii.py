class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        res= 0
        for i in range(len(prices)):
            if prices[i-1] and prices[i]<prices[i-1]:
                mini= prices[i]
            if prices[i]- mini>0:
                res+=prices[i]-mini
            mini= prices[i]
        return res