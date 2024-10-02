class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=float('inf')

        for price in prices:
            mini=min(price,mini)
            maxi=max(maxi,price-mini)
        return maxi