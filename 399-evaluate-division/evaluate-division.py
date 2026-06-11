class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj= defaultdict(list)
        for i, eq in enumerate(equations):
            m,n= eq
            adj[m].append([n, values[i]])
            adj[n].append([m, 1/values[i]] )

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q,visited= deque(), set([src])
            q.append([src, 1])
            while q:
                d,w= q.popleft()
                if d==target:
                    return w
                for nei,weight in adj[d]:
                    if nei not in visited:
                        q.append([nei, weight*w])
                        visited.add(nei)

            return -1
        return [bfs(a,b) for a,b in queries]