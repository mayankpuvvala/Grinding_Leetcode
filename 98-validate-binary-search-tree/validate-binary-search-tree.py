# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(node, low, high):
            if node is None:
                return True
            if not low< node.val< high:
                return False
            return search(node.left, low, node.val) and search(node.right, node.val, high)
        return search(root, float('-inf'), float('inf'))