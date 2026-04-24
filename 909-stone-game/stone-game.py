class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        from functools import lru_cache
        @lru_cache(None)
        def traverse(i,j):
            if i>j:
                return 0
            return max(
            piles[i]- traverse(i+1, j) ,
            piles[j]- traverse(i, j-1))
        return traverse(0,len(piles)-1)>0
