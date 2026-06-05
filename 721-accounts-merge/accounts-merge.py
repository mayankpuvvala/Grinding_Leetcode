class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name= {}
        graph= defaultdict(set)
        for account in accounts:
            name= account[0]
            for email in account[1:]:
                email_to_name[email]= name
                graph[account[1]].add(email)
                graph[email].add(account[1])

        visited= set()
        def dfs(email):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor)
        res= []
        for email, name in email_to_name.items():
            if email in visited:
                continue
            component= []
            dfs(email)
            res.append([name]+ sorted(component))
        return res

            