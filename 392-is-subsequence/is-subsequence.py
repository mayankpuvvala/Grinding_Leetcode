class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        find=[]
        i,j=0,0
        while i<len(t) and j<len(s):
            find.append(s[j])
            if t[i]==s[j]:
                j+=1
            i+=1


        return j==len(s)
