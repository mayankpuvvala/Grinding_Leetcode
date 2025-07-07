class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res= []
        subset= []
        def palindrome(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def dfs(i):
            if i==len(s):
                res.append(subset.copy())
                return 
            for j in range(i,len(s)):
                if palindrome(i,j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
        dfs(0)
        return res
