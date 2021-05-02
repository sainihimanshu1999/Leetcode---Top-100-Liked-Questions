def serializing(self,root):
    if not root: return '#'

    return ','.join([str(root.val),self.serializing(root.left),self.serializing(root.right)])

def derserialize(selr,data):
    self.data = data
    if self.data[0] == '#':
        return None

    node = TreeNode(self.data[:self.data.find(',')])
    node.left = self.derserialize(self.data[self.data.find(',')+1:])
    node.right = self.derserialize(self.data[self.data.find(',')+1:])

    return node
