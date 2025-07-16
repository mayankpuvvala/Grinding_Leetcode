class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res= []
        col = set()
        positive= set()
        negative= set()
        board= [["."]*n for _ in range(n)]
        def backtrack(r):
            if r==n:
                copy= ["".join(row) for row in board]
                res.append(copy)
                return res
            for c in range(n):
                if c in col or (r+c) in positive or (r-c) in negative:
                    continue
                col.add(c)
                positive.add(r+c)
                negative.add(r-c)
                board[r][c]="Q"

                backtrack(r+1)

                col.remove(c)
                positive.remove(r+c)
                negative.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res


