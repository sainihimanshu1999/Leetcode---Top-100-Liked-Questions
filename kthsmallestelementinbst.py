def kthsmallestelement(self,root):
    a = []
    def ino(root,a):
        if root:
            ino(root.left)
            a.append(root.val)
            ino(root.right)
    ino(root,a)
    return a[k-1]