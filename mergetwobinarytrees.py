def mergeTrees(self,root1,root2):
    if root1 and root2:
        root = TreeNode(root1.val + root2.val)
        root.left = mergeTrees(root1.left,root2.left)
        root.left = mergeTrees(root1.right,root2.right)
    else:
        return root1 or root2