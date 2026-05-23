class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        from collections import deque
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        minutes, fresh= 0, 0
        queue= deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        while queue and fresh>0:
            for _ in range(len(queue)):
                i,j= queue.popleft()
                for di,dj in directions:
                    di,dj= di+i, dj+j
                    if di<0 or di==rows or dj<0 or dj==cols or grid[di][dj]!=1:
                        continue
                    fresh-=1
                    queue.append((di,dj))
                    grid[di][dj]=2
            minutes+=1
        return minutes if fresh==0 else -1