'''
This answer is inspired from ever increasing triplet subsequence
'''

def subsequence(self,nums):
    sub = []

    for num in nums:
        pos,sub_len = 0,len(sub)

        while pos<=sub_len:
            if pos == sub_len:
                sub.append(num)
                break
            elif num<=sub[pos]:
                sub[pos] = num
                break
            else:
                pos += 1
    return len(sub)