def subsets(self,nums):
    if len(nums) == 0:
        return [[]]

    x = [[]]
    for i in range(len(nums)):
        for j in range(len(x)):
            x.append(x[j]+[nums[i]])

    x.sort()
    return x