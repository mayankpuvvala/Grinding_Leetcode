class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total= sum(matchsticks)
        if total%4!=0:
            return False
        target= total//4
        used = [False]*len(matchsticks)
        def dfs(i, k, sumi):
            if k==0:
                return True
            if sumi==target:
                return dfs(0,k-1, 0)
            for j in range(i,len(matchsticks)):
                if used[j] or sumi+matchsticks[j]>target:
                    continue
                used[j]=True
                if dfs(j+1, k, sumi+matchsticks[j]):
                    return True
                used[j]=False
                if sumi==0:
                    break
            return False
        return dfs(0,4,0)
