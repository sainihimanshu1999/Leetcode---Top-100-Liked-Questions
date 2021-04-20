'''
New Solution
This is also dp programming
'''

def palindromicSubstring(self,s):
    n = len(s)
    #intiating a DP
    dp = [[False]*n for _ in range(n)]

    #single element is always palindromic 
    ans = ''
    for i in range(n):
        dp[i][i] = True
        ans = s[i]

    maxLen = 1
    #starting from bottom and keep comparing
    for start in range(n-1,-1,-1):
        for end in range(start+1,n):
            if dp[start] == dp[end]:
                if start-end == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    if maxLen< end-start+1:
                        maxLen = end - start+1
                        ans = s[start:end+1]
    return ans













'''
Old solution
This approach is using dynamic programming using the table approach, it's quite complex indeed
'''


def longestPalindrome(self, s):
        n = len(s)
        
        table = [[0 for x in range(n)]for y in range(n)]
        maxLength = 1
        i = 0
        while(i<n):
            table[i][i] = True
            i = i+1
        start = 0
        i = 0
        while i<n-1:
            if(s[i]==s[i+1]):
                table[i][i+1] = True
                start = i
                maxLength =2
            i = i+1
        k=3
        while k <=n:
            i = 0
            while i<(n-k+1):
                j = i+k -1
                if(table[i+1][j-1] and s[i]==s[j]):
                    table[i][j] = True
                    if(k>maxLength):
                        start = i
                        maxLength = k
                i = i+1
            k = k+1
        return s[start:start+maxLength]