class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe= set()
        for idx,values in enumerate(graph):
            if values== []:
                safe.add(idx)
        visited= set()
        def dfs(i):
            if i in safe:
                return True
            if i in visited:
                return False
            visited.add(i)
            if all(dfs(j) for j in graph[i]):
                safe.add(i)  # to add the safe nodes which can reach terminal
                visited.remove(i) # to check cycles in only current path, hence, removed after path is completed
                return True
            visited.remove(i)
            return False
        for i in range(len(graph)):
            dfs(i)
        return sorted(safe)

