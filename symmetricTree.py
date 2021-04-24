def issymmetric(self,root):

    def mirror(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        if left.val == right.val:
            outpair = mirror(left.left,right.right)
            inpair = mirror(left.right,right.left)
            return outpair and inpair
        else:
            return False


    if root is None:
        return True
    else:
        return mirror(root.left,root.right)