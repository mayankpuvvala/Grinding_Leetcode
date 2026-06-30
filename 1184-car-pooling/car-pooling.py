class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi= float('-inf')
        maxi=  max(maxi, max(c for _,_,c in trips))
        newt= [0]*maxi
        for a,b,c in trips:
            for i in range(b,c):
                newt[i]+=a
                if newt[i]>capacity:
                    return False
        return True