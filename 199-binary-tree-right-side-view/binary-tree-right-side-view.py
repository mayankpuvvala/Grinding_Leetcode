# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        queue= collections.deque()
        queue.append(root)
        while queue:
            levels=[]
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    levels.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if levels:
                res.append(levels[-1])
        return res
