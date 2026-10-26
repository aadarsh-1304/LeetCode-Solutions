class Solution(object):
    def countIslands(self, grid, k):
        m, n=len(grid), len(grid[0])
        count=0
        def dfs(r, c):
            if r<0 or r>=m or c<0 or c>=n:
                return 0
            if grid[r][c]==0:
                return 0
            value=grid[r][c]
            grid[r][c]=0
            value+=dfs(r-1, c)
            value+=dfs(r+1, c)
            value+=dfs(r, c-1)
            value+=dfs(r, c+1)
            return value
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    total=dfs(i, j)
                    if total%k==0:
                        count+=1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna