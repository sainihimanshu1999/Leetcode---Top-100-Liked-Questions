'''
Using dfs and back tracking
'''

def combination(self,candidates,target):
    op = []

    def dfs(nums,target,path,op):
        if target<0:
            return

        if target == 0:
            op.append(path)
            return

        for i in range(len(nums)):
            dfs(nums[i:],target-nums[i],path+[nums[i]],op)

    dfs(candidates,target,[],op)
    return op
