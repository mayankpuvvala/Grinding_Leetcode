class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        made = set()

        changed = True

        while changed:
            changed = False

            # forward
            for i in range(len(recipes)):
                if recipes[i] in made:
                    continue

                if all(x in available for x in ingredients[i]):
                    available.add(recipes[i])
                    made.add(recipes[i])
                    changed = True

            # backward
            for i in range(len(recipes) - 1, -1, -1):
                if recipes[i] in made:
                    continue

                if all(x in available for x in ingredients[i]):
                    available.add(recipes[i])
                    made.add(recipes[i])
                    changed = True

        return list(made)