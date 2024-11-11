# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = []
        queue= deque([root])
        def bfs(node):
            if node is None:
                return 0
            while queue:
                level_size= len(queue)
                levels=[]
                for _ in range(level_size):
                    node = queue.popleft()
                    levels.append(node.val)
                    if node.left:
                        queue.append(node.left)
                        # bfs(node.left)
                    if node.right:
                        queue.append(node.right)
                        # bfs(node.right)
                self.res.append(levels)
        bfs(root)
        return self.res[-1][0]

            
            