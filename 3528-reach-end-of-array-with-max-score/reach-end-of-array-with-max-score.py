class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        score= 0
        i,j=0,nums[0]
        n= len(nums)
        prev= nums[0]
        start= 0

        for i in range(len(nums)):
            
            if nums[i]>prev:
                score+=(i-start)*nums[start]
                start = i
                prev=nums[i]
        score+=((n-1)-start)*nums[start]

        return score