def haystack(self,nums):
    for i in range(0,len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle) == needle]:
            return i
    return -1