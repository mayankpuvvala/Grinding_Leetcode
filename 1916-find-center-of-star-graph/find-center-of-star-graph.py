class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        newt = defaultdict(int)
        for i,j in edges:
            newt[i]+=1
            newt[j]+=1
        curr= newt[0]
        res= 0
        for i in newt:
            if newt[i]>curr:
                curr= newt[i]
                res= i
        return res
