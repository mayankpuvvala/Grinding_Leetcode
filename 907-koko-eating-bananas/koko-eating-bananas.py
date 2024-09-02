class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i,j=1,max(piles)
        res= j
        while i<=j:
            hrs=0
            k= i+(j-i)//2
            for p in piles:
                hrs+=math.ceil(p/k)

            if hrs<=h:
                j=k-1
                res= min(res,k)
            else:
                i=k+1

        return res