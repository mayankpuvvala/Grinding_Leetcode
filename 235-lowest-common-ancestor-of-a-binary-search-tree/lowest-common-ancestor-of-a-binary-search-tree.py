# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search_min(root, val):
            path=[]
            while root:
                path.append(root.val)
                if val< root.val:
                    root = root.left
                elif val> root.val:
                    root= root.right
                else:
                    break
            return path
        res1= search_min(root, p.val)
        res2= search_min(root, q.val)
        res=[]
        for i, j in zip(res1, res2):
            if i==j:
                res.append(i)
            else:
                break
        return TreeNode(res[-1]) if res else None