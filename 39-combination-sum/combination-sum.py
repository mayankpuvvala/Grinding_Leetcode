class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, subset, total):
            if total==target:
                res.append(subset.copy())
                return
            elif i==len(candidates) or total>target:
                return
            for idx in range(i, len(candidates)):
                subset.append(candidates[idx])
                backtrack(idx, subset, total+candidates[idx])
                subset.pop()
        backtrack(0, [], 0)
        return res