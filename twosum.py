'''
Solving using hastable
'''

def twosum(self,nums,target):
    dic= {}
    for index,value in enumerate(nums):
        m = target-value
        if m in dic:
            return[dic[m],index]
        else:
            dic[value] = index