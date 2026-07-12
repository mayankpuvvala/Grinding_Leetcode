class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries= sorted(range(len(queries)), key= lambda i:queries[i])
        intervals.sort()
        newt= []
        res= [-1]*len(queries)
        i=0
        for idx in sorted_queries:
            q= queries[idx]
            while i<len(intervals) and intervals[i][0]<=q:
                l,r = intervals[i]
                heapq.heappush(newt, (r-l+1, r))
                i+=1
            while newt and newt[0][1]<q:
                heapq.heappop(newt)
            if newt:
                res[idx] = newt[0][0]
                
        return res

