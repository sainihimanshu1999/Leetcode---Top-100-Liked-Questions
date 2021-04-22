def watertrapping(self,nums):
    leftmaxnums = [0]*len(nums)
    rightmaxnums = [0]*len(nums)
    water = [0]*len(nums)

    maxLeft = 0 
    maxRight = 0
    for i in range(len(nums)):
        maxLeft = max(maxLeft,nums[i])
        leftmaxnums[i] = maxLeft
    
    for i in range(len(nums)-1,-1,-1):
        maxRight = max(maxRight,nums[i])
        rightmaxnums[i] = maxRight

    for i in range(len(nums)):
        water[i] = min(leftmaxnums[i],rightmaxnums[i]) - nums[i]

    return sum(water)
