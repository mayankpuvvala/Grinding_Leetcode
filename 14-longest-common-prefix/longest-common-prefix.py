class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res= ""
        strs.sort()
        if len(strs)==1:
            return str(strs[0])
        first,last = strs[0],strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                break
            res+=first[i]
        return res