'''
naive soltuion using recursion, but time limit exceeded
'''

def editDistance(self,word1,word2):
    if not word1 and not word2:
        return 0

    if not word1:
        return len(word2)

    if not word2:
        return len(word1)

    if word1[0] == word2[0]:
        return self.editDistance(word1[1:],word2[1:])
    
    insert = 1 + self.minDistance(word1,word2[1:])
    delete = 1 + self.minDistance(word1[1:],word2)
    replace = 1 + self.minDistance(word1[1:],word2[1:])

    return min(insert, delete, replace)


'''
DP (Memoization) soltuion because in upper solution time limit get exceeded
'''

def editDistance(word1,word2,i,j,memo):
    if i == len(word1) and j ==len(word2):
        return 0
    
    if i == len(word1):
        return len(word2)-j

    if j == len(word2):
        return len(word1) - i

    if (i,j) not in memo:
        if word1[i] == word2[j]:
            ans = editDistance(word1, word2, i+1, j+1, memo)

        else:
            insert = editDistance(word1,word2,i,j+1,memo)
            delelte = editDistance(word1,word2,i,j+1,memo)
            repplace = editDistance(word1,word2,i+1,j+1)
            ans = min(insert,delelte,repplace)
        memo[(i,j)] = ans
    return memo[(i,j)]
