class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, subset, total):
            if total==target:
                res.append(subset.copy())
                return
            elif i==len(candidates) or total>target:
                return
            subset.append(candidates[i])
            backtrack(i, subset, total+candidates[i])
            subset.pop()
            backtrack(i+1, subset, total)
        backtrack(0,[],0)
        return res