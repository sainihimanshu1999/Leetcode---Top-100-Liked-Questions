def inorderTraversal(self,root):
    def ino(root,ans):
        if root:
            ino(root.left,ans)
            ans.append(root.val)
            ino(root.right.ans)
        return ans
    
    return ino(root,[])