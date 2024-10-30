# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def height(node, max_val):
            if node is None:
                return 0
            res= 1 if node.val>= max_val else 0
            max_val = max(max_val, node.val)
            res+= height(node.left, max_val)
            res+= height(node.right, max_val)
            return res
        return height(root, root.val)