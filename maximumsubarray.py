'''
This is solved using kadane's algorithim
'''

def maximumsubarray(self,nums):
    for i in range(1,len(nums)):
        if nums[i-1]>0:
            nums[i] = nums[i-1]+nums[i]

    return max(nums)