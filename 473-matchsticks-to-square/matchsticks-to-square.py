class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #basically, we have to get 4 subsets with sum = sum//4
        total_sum= sum(matchsticks)
        target= total_sum//4
        if (total_sum %4)!=0:
            return False
        used= [False]*len(matchsticks)
        def dfs(i, k, subset_sum):
            if k==0:
                return True
            if subset_sum==target:
                return dfs(0,k-1,0)
            for j in range(i,len(matchsticks)):
                if used[j] or subset_sum + matchsticks[j] >target:
                    continue
                used[j]=True
                if dfs(j+1, k, subset_sum +  matchsticks[j]):
                    return True
                used[j]=False
                if subset_sum==0:
                    break
            return False   
            
        return  dfs(0,4,0)
            