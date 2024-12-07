class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res= []
        def dfs(i,subset):
            if i==len(s):
                res.append(subset)
                return 
            if (s[i]<="9" and s[i]>="0"):
                dfs(i+1,subset+s[i])
            else:
                dfs(i+1, subset+s[i].lower())
                dfs(i+1, subset+s[i].upper())
        dfs(0,"")
        return res
