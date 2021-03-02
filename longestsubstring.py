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