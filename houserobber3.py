'''
House robber 3- robbery in a tree, only constraint is that robber can't rob directly linked treenode
'''

def rob(self,root):
    def superchor(node):
        if not node:
            return (0,0)

        left,right = superchor(node.left),superchor(node.right)

        now = node.val + left[1]+right[1]

        later = max(left)+max(right)

        return (now,later)
    return max(superchor(root))