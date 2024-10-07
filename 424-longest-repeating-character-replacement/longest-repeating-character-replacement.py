class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        newt= defaultdict(int)
        maxf=0
        i,j=0,0
        count=0

        while j<len(s):
            newt[s[j]]+=1
            maxf= max(maxf,newt[s[j]])

            if (j-i+1)-maxf >k:
                newt[s[i]]-=1
                i+=1
            
            count= max(j-i+1,count)
            j+=1
        return count
