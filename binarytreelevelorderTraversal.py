def traversal(self,root):
    ans = []
    level = [root]

    while root and level:
        currentNode = []
        nextLevel = []
        for node in level:
            currentNode.append(node.val)

            if node.left:
                nextLevel.append(node.left)
            
            if node.right:
                nextLevel.append(node.right)

        ans.append(currentNode)
        level = nextLevel
    return ans