class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total%4!=0:
            return False
        target= total//4
        matchsticks.sort(reverse= True)
        used= [False]*len(matchsticks)
        def dfs(i, sumi, k):
            if k==0:
                return True
            if sumi==target:
                return dfs(0, 0, k-1)
            for j in range(i, len(matchsticks)):
                if used[j] or sumi+matchsticks[j]>target:
                    continue
                if j>0 and matchsticks[j]==matchsticks[j-1] and not used[j-1]:
                    continue
                used[j]= True
                if dfs(j+1, sumi+matchsticks[j], k):
                    return True
                used[j]= False
                if sumi==0:
                    break
            return False
        return dfs(0, 0, 4)
