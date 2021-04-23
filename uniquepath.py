'''
Using dp, O(m*n) space time complexity
'''

def uniquePath(self,row,col):
    if not row or not col:
        return 0

    dp = [[1]*col for i in range row]

    for i in range(1,row):
        for j in range(1,col):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]


'''
similarly using dp but with O(n) space
'''

def uniquePath(self,row,col):

    if not row or not col:
        return 0

    curr = [1]*col

    for i in range(1,row):
        for j in range(1,col):
            curr[j] += curr[j-1]
    return curr[-1]