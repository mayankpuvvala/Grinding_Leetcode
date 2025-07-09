class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        nums.sort(reverse=True)
        target= sum(nums)//k
        subset= []
        used= [False]*len(nums)
        res= 0
        def dfs(i, k, subsetSum):
            if k==0:
                return True
            if subsetSum==target:
                return dfs(0,k-1, 0)
            for j in range(i,len(nums)):
                if used[j] or nums[j]+subsetSum >target:
                    continue
                used[j]=True
                if dfs(j+1, k, subsetSum+nums[j]):
                    return True
                used[j]=False
                if subsetSum==0:
                    break
            return False
        return dfs(0,k,0)
                
            
