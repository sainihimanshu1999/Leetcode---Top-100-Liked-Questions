def palindromicsusbtring(self,s):
    if not s:
        return 0

    n = len(s)

    table = [[False]*n for _ in range(n)]

    #for single element
    for i in range(n):
        table[i][i] = True
        count += 1

    #for sliding window of size 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            count += 1

    #for sliding window of size 3
    for k in range(3,n+1):
        for i in range(n-k+1):
            j = i+k-1
            if table[i+1][j-1] and s[i]==s[j]:
                table[i][j] = True
                count += 1

    return count