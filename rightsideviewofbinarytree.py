def rightsideview(self,root):
    if not root:
        return []

    right = self.rightsideview(root.right)
    left = self.rightsideview(root.left)

    return [root.val]  + right + left[len(right):]