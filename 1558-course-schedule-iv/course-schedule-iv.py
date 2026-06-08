class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        directions = defaultdict(list)
        for j,i in prerequisites:
            directions[i].append(j)
        preMap = {}
        def dfs(i):
            if i not in preMap:
                preMap[i] = set()
                for j in directions[i]:
                    preMap[i] |= dfs(j)
                preMap[i].add(i)
            return preMap[i]

        for i in range(numCourses):
            dfs(i)
        
        res = []
        for u,v in queries:
            res.append(u in preMap[v])
        return res
        