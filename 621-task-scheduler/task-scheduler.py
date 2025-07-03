class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        newt= defaultdict()
        for i in tasks:
            newt[i]= newt.get(i,0)+1
        maxHeap = [-i for i in newt.values()]
        heapq.heapify(maxHeap)
        time= 0
        q= deque()
        while maxHeap or q:
            time= time+1
            if maxHeap:
                first= heapq.heappop(maxHeap) +1
                if first!=0:
                    q.append([first, time+n])
            if q and time==q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time
