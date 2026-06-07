class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq= defaultdict(list)
        for i,j in prerequisites:
            prereq[i].append(j)
        cycle, visited= set(), set()
        output= []
        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            cycle.add(i)
            for j in prereq[i]:
                if dfs(j)== False:
                    return False
            cycle.remove(i)
            visited.add(i)
            output.append(i)
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return output
        
