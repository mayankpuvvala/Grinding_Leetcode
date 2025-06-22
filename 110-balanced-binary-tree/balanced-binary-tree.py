# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height= 0
        def dfs(node):
            if not node:
                return 0
            left= dfs(node.left)
            right= dfs(node.right)
            if abs(left-right)>1:
                self.height=2
            return 1+ max(left,right)
        dfs(root)
        return True if self.height<2 else False