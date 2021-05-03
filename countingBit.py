def countingBit(self,num):
    result = [0]
    while len(result) <= num:
        result += [i+1 for i in result]

    return result[:num+1]