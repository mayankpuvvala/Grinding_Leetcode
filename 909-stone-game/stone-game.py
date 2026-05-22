class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def traverse(i,j):
            if i>j:
                return 0
            return max(
                    piles[i]- traverse(i+1, j),
                    piles[j]- traverse(i,j-1)) #idea is that don't take the curr element again in the scope, hence, shifting the pointers
        return traverse(0,len(piles)-1) > 0
        #or just return True