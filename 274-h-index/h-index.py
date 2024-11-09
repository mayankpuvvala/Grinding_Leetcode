class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==1:
            if citations[0]==0:
                return 0
            if citations[0]>0:
                return 1
        citations.sort()
        total= len(citations)-1
        for idx,i in enumerate(citations) :
            h=i
            if h>total-idx:
                h= citations[idx-1] if idx>0 else 0
                while h<=total-idx:
                    h+=1
                return h

        return 0