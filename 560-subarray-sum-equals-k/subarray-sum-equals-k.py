class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_sum= 0
        prefix_sum_count= {0:1}
        for i in nums:
            prefix_sum+=i
            if prefix_sum-k in prefix_sum_count:
                count+= prefix_sum_count[prefix_sum - k]
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum]+=1
            else:
                prefix_sum_count[prefix_sum]=1
        return count