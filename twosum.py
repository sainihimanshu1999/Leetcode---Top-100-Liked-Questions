def twoSum(self, nums, target):
        a = {}
        for i,n in enumerate(nums):
            m = target - n
            if m in a:
                return [a[m],i]
            else:
                a[n] = i

'''
using hash table approach to reduce the time complexity
'''