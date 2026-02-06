class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low<= high:
            k= (low+high)//2
            res= 0
            for i in piles:
                res+= ceil(i/k)
            if res<=h:
                high = k -1 
            else : 
                low = k+1
        return low