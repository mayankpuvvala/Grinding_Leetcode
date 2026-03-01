# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val!=b.val:
                return False
            return dfs(a.left, b.left) and dfs(a.right, b.right)
        
        def subtree(p,q):
            if not p:
                return False
            if dfs(p,q):
                return True
            return subtree(p.left, q) or subtree(p.right, q)
        return subtree(root, subRoot)
        