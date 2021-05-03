def topKfrequentelement(self,nums,k):
    a = []
    dic = {}
    for num in nums:
        dic[num] = dic.get(num,0)+1
    a = sorted(dic,key=dic.get,reverse=True)
    return a[:k]