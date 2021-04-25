def buildTree(self,preorder,inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[index])
        root.left = self.buildTree(preorder,inorder[0:index])
        root.right = self.buildTree(preorder,inorder[index+1:])
    return root