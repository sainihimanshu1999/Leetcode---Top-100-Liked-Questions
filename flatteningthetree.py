def flatten(self,root):
    while root:
        if root.left:
            self.flatten(root.left)
            tail = root.left
            while tail.right:
                tail = tail.right
            tail.right = root.right
            root.right = root.left
            root.left = None
        root = root.right
