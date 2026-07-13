class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms= [[0] for _ in range(n)]
        for l, r in meetings:
            i=0 
            while i<n and rooms[i][-1]>l:
                i+=1
            if i<n:
                rooms[i].append(r) #since, rooms' previous value; rooms[i][-1]<=l, so, we will use r anyways, without more math
            else:
                i= min(range(n), key= lambda k:rooms[k][-1])
                rooms[i].append(rooms[i][-1] + r-l)

        maxi= max(len(room) for room in rooms)
        for i in range(n):
            if len(rooms[i])==maxi:
                return i
        
            

