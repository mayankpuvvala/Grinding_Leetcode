class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini= float('inf')
        sum=0
        profit=0
        for price in prices:
            mini= min(mini, price)
            profit= price - mini
            sum+=profit
            mini= price
        return sum