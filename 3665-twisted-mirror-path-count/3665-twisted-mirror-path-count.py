class Solution(object):
    def uniquePaths(self, grid):
        MOD=10**9+7
        m, n=len(grid), len(grid[0])
        right=[[None]*n for _ in range(m)]
        down=[[None]*n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]==0:
                    right[i][j]=(i, j)
                    down[i][j]=(i, j)
                else:
                    if i+1<m:
                        right[i][j]=down[i+1][j]
                    if j+1<n:
                        down[i][j]=right[i][j+1]
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if dp[i][j]==0:
                    continue
                ways=dp[i][j]
                if j+1<n:
                    dest=right[i][j+1]
                    if dest is not None:
                        x, y=dest
                        dp[x][y]=(dp[x][y]+ways)%MOD
                if i+1<m:
                    dest=down[i+1][j]
                    if dest is not None:
                        x, y=dest
                        dp[x][y]=(dp[x][y]+ways)%MOD
        return dp[m-1][n-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna