class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col= len(board),len(board[0])
        def capture(r,c):
            if r<0 or r==row or c<0 or c==col or board[r][c]!="O":
                return 
            board[r][c]="T"
            capture(r-1,c)
            capture(r+1,c)
            capture(r,c+1)
            capture(r,c-1)

        for i in range(row):
            for j in range(col):
                if board[i][j]=="O" and (i in [0, row-1] or j in [0,col-1]):
                    capture(i,j)
        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="T":
                    board[i][j]="O"