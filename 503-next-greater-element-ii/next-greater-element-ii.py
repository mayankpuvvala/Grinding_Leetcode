class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res= [-1]*len(nums)
        for idx, i in enumerate(nums):
            while stack and nums[stack[-1]]<i:
                res[stack.pop()]=i
            stack.append(idx)
        
        for i in nums:
            while stack and nums[stack[-1]]<i:
                res[stack.pop()]=i
        
        return res
