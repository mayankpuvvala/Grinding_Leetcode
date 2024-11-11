# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res =[]
        def preorder(node):
            if node is None:
                return 
            self.res.append(node.val)
            node.left= preorder(node.left)
            node.right = preorder(node.right)

        preorder(root)
        return self.res