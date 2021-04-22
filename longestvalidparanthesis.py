def longestvalidparanthesis(self,s):
    if not s:
        return 0

    stack = []
    dp = [0]*len(s)

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
            continue
            
        if stack:
            leftIndex = stack.pop()
            dp[i] = i-leftIndex+1+dp[leftIndex-1]
    return max(dp)