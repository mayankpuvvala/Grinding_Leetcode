class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        newt={}
        for i in arr:
            newt[i]= newt.get(i,0)+1
        
        res= set(newt.values())
        return len(res)==len(newt.values())

        # for i in newt.values():
        #     if i in res:
        #         return False
        #     res.append(i)
        # return True
