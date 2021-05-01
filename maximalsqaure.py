'''
dynamic programming approach is used to solve this question
'''
def maximalsquare(self,grid):
    if not grid or len(grid)<1:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    maxside = 0
    dp = [[0]*(cols+1) for _ in range(rows+1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dp[r+1][c+1] = min(dp[r][c],dp[r+1][c],dp[r][c+1]) + 1
                maxside = max(maxside,dp[r+1][c+1])

    return maxside*maxside