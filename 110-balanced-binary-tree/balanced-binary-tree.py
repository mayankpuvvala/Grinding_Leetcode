# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.length=0
        def depth(node):
            if not node:
                return 0
            
            left= depth(node.left)
            right= depth(node.right)

            # self.length= min(self.length, abs(left-right))
            if abs(left-right)>1:
                self.length=2
            return 1+max(left,right)
        depth(root)
        return self.length<=1