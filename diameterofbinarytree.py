def diameterofbinaryTree(self,root):
    self.answer = 0
    def depth(node):
        if not node:
            return 0

        left,right = depth(node.left),depth(node.right)
        self.answer = max(self.answer,left+right)
        return 1+max(left,right)

    depth(root)
    return self.answer