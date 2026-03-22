class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res= []
        def backtrack(subset, open, close):
            if open==close and close==n:
                res.append("".join(subset))
                return
            if open<n:
                subset.append("(")
                backtrack(subset, open+1, close)
                subset.pop()
            if open>close:
                subset.append(")")
                backtrack(subset, open, close+1)
                subset.pop()
        backtrack([], 0, 0)
        return res