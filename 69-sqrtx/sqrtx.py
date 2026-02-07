class Solution:
    def mySqrt(self, x: int) -> int:
        i,j= 1, x
        ans =0
        while i<=j:
            mid= i+ (j-i)//2
            if mid==x/mid:
                return mid
            elif mid< x/mid:
                ans= mid
                i= mid+1
            else:
                j= mid-1
        return ans