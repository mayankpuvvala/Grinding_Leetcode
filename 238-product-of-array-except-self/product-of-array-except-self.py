class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length= len(nums)
        newt=[1]*length

        
        for i in range(1,length):
            newt[i]=newt[i-1]*nums[i-1]

        right=1
        for i in range(length-1,-1,-1):
            newt[i]*=right
            right*=nums[i]

        return newt

        