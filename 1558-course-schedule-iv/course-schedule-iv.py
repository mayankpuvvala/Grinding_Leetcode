class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj= defaultdict(list)
        for i,j in prerequisites:
            adj[i].append(j)
        # 0:[], 1: [0,2], 2: [0]
        # if 1, we'll check all prereq and their prereq if any, and if they have the value 1, then we return False
        visited= set()
        carries = defaultdict(set)
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in adj[i]:
                dfs(nei)
                carries[i].add(nei)
                carries[i].update(carries[nei]) #bubble backward, by adding the nei connections to i

        for i in range(numCourses):
            dfs(i)
        res= []
        for i,j in queries:
            res.append(j in carries[i])
        return res