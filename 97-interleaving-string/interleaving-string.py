class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i,j):
            if i==len(s1) and j==len(s2):
                return True
            if i<len(s1) and s3[i+j]==s1[i]:
                if dfs(i+1, j):
                    return True
            if j<len(s2) and s3[i+j]==s2[j]:
                if dfs(i, j+1):
                    return True
            return False
        return dfs(0,0)