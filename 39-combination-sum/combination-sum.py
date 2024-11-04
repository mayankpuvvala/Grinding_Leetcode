class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i, sumi):
            if sumi == target:
                res.append(subset.copy())
                return 
            if sumi>target or i>=len(candidates):
                return 
            subset.append(candidates[i])
            dfs(i, sumi+candidates[i])
            subset.pop()
            dfs(i+1, sumi)
        dfs(0,0)
        return res