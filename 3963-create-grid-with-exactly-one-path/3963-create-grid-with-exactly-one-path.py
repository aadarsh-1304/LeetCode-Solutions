class Solution(object):
    def createGrid(self, m, n):
        grid=[['#']*n for _ in range(m)]
        i, j=0, 0
        grid[i][j]='.'
        while j<n-1:
            j+=1
            grid[i][j]='.'
        while i<m-1:
            i+=1
            grid[i][j]='.'
        return [''.join(row) for row in grid]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna