'''
Best approach is binary search
'''
def search(self,nums,target):
    if not nums:
        return -1
    
    low,high = 0 , len(nums)-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid

        if nums[low]<=nums[high]:
            if nums[low]<=target<=nums[mid]:
                high = mid -1
            else:
                low = mid+1
        else:
            if nums[mid]<=target<=nums[high]:
                low = mid+1
            else:
                high = mid-1

    return -1