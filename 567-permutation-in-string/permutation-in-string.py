class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        newt = defaultdict(int)
        for i in s1:
            newt[i]+=1

        i=0
        window = defaultdict(int)
        
        for j in range(len(s2)):
            window[s2[j]]+=1
            if (j-i+1)> len(s1):
                window[s2[i]]-=1
                if window[s2[i]]==0:
                    del window[s2[i]]
                i+=1
            if window== newt:
                return True
        return False
