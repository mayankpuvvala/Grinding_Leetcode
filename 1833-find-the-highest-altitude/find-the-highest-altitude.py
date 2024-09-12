class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi= -float('inf')
        sum=0
        for i in gain:
            sum+=i
            maxi= max(maxi,sum)
        return maxi if maxi>0 else 0
