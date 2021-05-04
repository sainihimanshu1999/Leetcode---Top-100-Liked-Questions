'''
Technique of neagtion is used in this, as we move in the array, we make the number present at the index 
equal to the current number we at, and just return index+1 of the positive number present in array after
traversing the array
'''

def finidingdisappearednumbers(self,nums):
    for i in range(len(nums)):
        index = abs(nums[i])
        nums[index] = -abs(nums[index])
    
    return [i+1 for i in range(len(nums)) if nums[i]>0]