class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        canCook= set()
        visited = set()
        newt = {r:i for i,r in enumerate(recipes)}
        def dfs(i):
            if i in canCook:
                return True
            if i in visited:
                return False
            visited.add(i)
            for j in ingredients[i]:
                if j in supplies:
                    continue
                if j in newt:
                    if not dfs(newt[j]):
                        visited.remove(i)
                        return False
                else:
                    visited.remove(i)
                    return False

            canCook.add(i)
            visited.remove(i)
            return True
            
        return [recipes[i] for i in range(len(recipes)) if dfs(i)]
        