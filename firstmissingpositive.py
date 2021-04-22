'''
it's a leetcode hard question, i am truly amazed at thsi solution
'''


def solve(self,nums):
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res+=1
    return res