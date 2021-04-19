'''
New solution
'''

def longestsubstring(self,A):
    used = {}
    start = maxlength = 0

    for index,char in enumerate(A):
        if char in used and start<=used[char]:
            start = used[char]+1
        else:
            maxlength = max(maxlength,index-start+1)
        used[char] = index

    return maxlength




'''
old solution
'''

def lengthOfLongestSubstring(self, s):
        lastIndex = [-1]*256
        n = len(s)
        res = 0
        i = 0
        
        for j in range(0,n):
            i = max(i, lastIndex[ord(s[j])] +1)
            res = max(res,j-i+1)
            
            lastIndex[ord(s[j])] = j
            
        return res

'''
time complexity is O(n+d) i.e linear time complexity
sliding window approach has been used in this solution
'''