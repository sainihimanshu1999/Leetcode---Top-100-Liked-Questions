def maximumprod(self,nums):
    b = nums[::-1]
    for i in range(1,len(nums)):
        nums[i] *= nums[i-1] or 1
        b[i] *= b[i-1] or 1
    return max(nums+b)