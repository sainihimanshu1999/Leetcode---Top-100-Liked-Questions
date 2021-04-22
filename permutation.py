def permute(self,nums):
    result = []
    self.dfs(nums,[],result)
    return result

def dfs(self,nums,path,result):
    if not nums:
        result.append(path)

    for i in range(len(nums)):
        self.dfs(nums[:1]+nums[i+1:],path+[nums[i]],result)