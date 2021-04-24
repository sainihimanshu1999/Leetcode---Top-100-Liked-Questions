def validbst(self,root):
    def bst(node,left,right):
        if not node:
            return True
        
        if not left<node.val<right:
            return False

        return bst(node.left,left,node.val) and bst(node.right,node.val,right)

    return bst(root,float('-inf'),float('inf'))