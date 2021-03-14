class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a = [[]]
        for i in range(len(nums)):
            for j in range(len(a)):
                a.append(a[j]+[nums[i]])
        return a
        