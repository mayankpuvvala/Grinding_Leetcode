class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maxi= -float('inf')
        for i in arr:
            maxi= max(maxi,i)
        newt= []
        for i in range(1,maxi):
            newt.append(i)
        res= []
        i,j=0,0
        while j<len(arr) and i<len(newt):
            if newt[i]!=arr[j]:
                res.append(newt[i])
                i+=1
            else:
                i+=1
                j+=1
        while len(res)<k:
            res.append(maxi+1)
            maxi+=1
        ans= res[k-1]
        return ans
