def duplicate(self,nums):
    dic = {}
        
    for num in nums:
        dic[num] = dic.get(num,0)+1
        
    for key,value in dic.items():
        if value>1:
            return key