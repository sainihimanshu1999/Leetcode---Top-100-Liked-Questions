'''
Simple recursion appraoch towards 0/1 knapsack problem
'''

def targetSum(self,nums,target):
    index = len(nums)-1
    curr_sum = 0
    return self.dp(nums,target,index,curr_sum)

def dp(self,nums,target,index,curr_sum):
    if index<0 and curr_sum==target:
        return 1
    
    if index<0:
        return 0

    postive = self.dp(nums,target,index-1,curr_sum+nums[index])
    negative = self.dp(nums,target,index-1,curr_sum+ -nums[index])

    return postive+negative


'''
optimizing the above appraoch using memoization
'''

def targetSum(self,nums,target):
    index = len(nums)-1
    curr_sum = 0
    self.memo = {}
    return self.dp(nums,target,index,curr_sum)


def dp(self,nums,target,index,curr_sum):
    if(index,curr_sum) in self.memo:
        return self.memo[(index,curr_sum)]

    if index<0 and curr_sum ==  target:
        return 1

    if index<0:
        return 0

    positive = self.dp(nums,target,index-1,curr_sum+nums[index])
    negative = self.dp(nums,target,index-1,curr_sum+ -nums[index])

    self.memo[(index,curr_sum)] = positive+negative
    return self.memo[(index,curr_sum)]
