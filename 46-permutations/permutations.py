class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset= []
        def backtrack():
            if len(subset.copy())==len(nums):
                res.append(subset.copy())
                return
            
            for i in nums:
                if i not in subset:
                    subset.append(i)
                    backtrack()
                    subset.pop()
        backtrack()
        return res