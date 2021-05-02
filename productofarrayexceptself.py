def prodofarr(self,nums):
    n = len(nums)
    result = []
    p =1

    for i in range(0,n):
        result.append(p)
        p = p*nums[i]


    p = 1

    for i in range(n-1,-1,-1):
        result[i] = result[i]*p
        p = p*nums[i]

    return result