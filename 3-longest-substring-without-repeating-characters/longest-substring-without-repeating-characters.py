class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        n= len(s)
        res= []
        maxi= 0
        while i<=j and j<n:
            if s[j] not in res:
                res.append(s[j])
                maxi= max(maxi, len(res))
                j+=1
            else:
                res.remove(s[i])
                i+=1
        return maxi
