# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.min_row, self.min_col, self.max_row, self.max_col= 0,0,0,0
        def dfs(row, col, node):
            if not node:
                return
            self.res.append([row,col, node.val])

            self.min_col= min(self.min_col, col)
            self.max_col= max(self.max_col, col)
            self.min_row= min(self.min_row, row)
            self.max_row= max(self.max_row, row)

            dfs(row+1, col-1, node.left)
            dfs(row+1, col+1, node.right)
        
        dfs(0,0,root)
        self.res.sort(key= lambda x:(x[1], x[0],x[2]))
        result= []
        for i in range(int(self.min_col), int(self.max_col+1)):
            levels= [ val for row, col, val in self.res if col==i]
            result.append(levels)
        return result
        