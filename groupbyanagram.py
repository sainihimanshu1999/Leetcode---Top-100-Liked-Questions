def groupbyanagram(self,strs):
    dic = {}

    for word in strs:
        key = tuple(sorted(word))
        dic[key] = dic.get(key,[]) + [word]
    return list(dic.values())