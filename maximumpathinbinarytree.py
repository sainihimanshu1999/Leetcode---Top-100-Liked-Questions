def maximumpath(self,root):
    max_path = float('-inf')

    def solve(self,node):
        nonlocal max_path

        if not node:
            return 0

        leftgain = max(solve(node.left),0)
        rightgain = max(solve(node.right),0)

        current_max_path = node.val +  leftgain + rightgain
        max_path = max(current_max_path,max_path)

        return node.val + max(leftgain,rightgain)
    solve(root)
    return max_path