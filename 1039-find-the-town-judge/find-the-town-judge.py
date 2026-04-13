class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc= defaultdict(int)
        out= defaultdict(int)
        for vals in trust:
            a,b= vals[0], vals[1]
            inc[b]+=1
            out[a]+=1
        for i in range(1,n+1):
            if inc[i]==n-1 and out[i]==0:
                return i
        return -1