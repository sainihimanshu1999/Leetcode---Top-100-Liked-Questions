'''
using catalan's number for counting unique bst, generating paranthesis, full binary trees
'''
'''
Normal forumla with recusrion
'''

def solve(n):
    if n<=1:
        return 1
    res = 0
    for i in range(n):
        res+= solve(i)*solve(n-i-1)


'''
dynamic programming approach
'''

def solve(n):
    if n == 0 or n==1:
        return 1
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]
