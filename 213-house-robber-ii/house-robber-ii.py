class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        def worker(start, end):
            three, two, one= 0,0,0
            for i in range(start, end, -1):
                one, two, three= nums[i]+ max(two, three), one, two
            return max(one, two)
        return max(
                worker(n-2, -1), 
                worker(n-1, 0)
                )
