'''
Just recursion, time complexity is O(n^2)
'''

def pathSum(self,root,targetSum):
    self.numberofPaths = 0

    self.dfs(root,targetSum)

    return self.numberofPaths

def dfs(self,node,target):
    if not node:
        return None

    self.test(node,target)
    self.dfs(node.left,target)
    self.dfs(node.right,target)


def test(self,node,target):

    if not node:
        return None

    if node.val == target:
        self.numberofPaths += 1

    self.test(node.left,target-node.val)
    self.test(node.right,target-node.val)


'''
Dp with memoization
'''

def pathSum(self,root,targetSum):
    self.result = 0
    dic = {0:1}
    self.dfs(root,targetSum,0,dic)

def dfs(root,target,currPathSum,dic):
    if not root:
        return None

    currPathSum += root.val
    oldpathsum = currPathSum-target

    self.result +=  dic.get(oldpathsum,0)
    dic[currPathSum] = dic.get(currPathSum,0)+1

    self.dfs(root.left,target,currPathSum,dic)
    self.dfs(root.right,target,currPathSum,dic)

    dic[currPathSum] -=1