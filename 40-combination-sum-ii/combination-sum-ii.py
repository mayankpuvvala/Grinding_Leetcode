class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset= []
        candidates.sort()
        def dfs(i, sumi):
            if sumi== target:
                res.append(subset.copy())
                return 
            if sumi>target or i>=len(candidates):
                return 
            subset.append(candidates[i])
            dfs(i+1, sumi+candidates[i])

            subset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, sumi)
        dfs(0,0)
        return res