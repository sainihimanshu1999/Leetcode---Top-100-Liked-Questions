'''
simple recursion
'''

def wordBreak(self,s,wordDict):
    if s == '':
        return True

    for word in wordDict:
        if s[:len(word)] == word:
            if len(s) == len(word):
                return True
            else:
                suffix = s[len(word):]
                if(self.wordBreak(suffix,wordDict)):
                    return True
    return False


'''
Dynamic Programming method
'''

def wordBreak(self,s,wordDict):
    dp = {}
    def wordBank(a):
        if a in dp:
            return dp[a]

        for word in wordDict:
            if a[:len(word)] ==  word:
                if len(a) == len(word):
                    dp[a] = True
                    return dp[a]

                else:
                    suffix = a[len(word):]
                    if(wordBank(suffix)):
                        dp[a] = True
                        return dp[a]
        dp[a] = False
        return dp[a]
    
    return wordBank(s)
