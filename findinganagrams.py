'''
Finding anagram and then returning the starting index of anagrams
'''
import collections
def FindingAnagram(self,s,p):
    x = collections.Counter(p)
    y = collections.Counter(s[:len(p)])

    i = 0
    j = len(p)
     
    result = []

    while j<=len(s):
        if x == y:
            result.append(i)

        y[s[i]]-=1
        if y[s[i]]<=0:
            y.pop(s[i])

        if j<len(s):
            y.[s[j]] += 1
        
        i+= 1
        j+=1
    return result