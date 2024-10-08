class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count= defaultdict(int)
        freq= [[] for i in range(len(nums)+1)]

        for x in nums:
            count[x] +=1

        for n,c in count.items():
            freq[c].append(n)
        
        res= []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res