def maxArea(self,matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    highs = [0]*(n+1)
    ans = 0
    for row in matrix:
        for i in range(n):
            highs[i] = highs[i] +1 if row=='1' else 0
        stack = [-1]
        for i in range(n+1):
            while highs[i]<highs[stack[-1]]:
                h = highs[stack.pop()]
                w = i-stack[i]-1
                ans = max(ans,h*w)
            stack.append(i)

    return ans