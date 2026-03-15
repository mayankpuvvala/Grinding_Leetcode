class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res= []
        def dfs(node):
            if not node:
                self.res.append("n")
                return 
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(self.res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data= data.split(",")
        self.i=0
        def dfs():
            if data[self.i]=="n":
                self.i+=1
                return None
            node= TreeNode(int(data[self.i]))
            self.i+=1
            node.left= dfs()
            node.right= dfs()
            return node
        return dfs()

        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))