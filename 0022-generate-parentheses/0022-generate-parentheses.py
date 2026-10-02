class Solution(object):
    def generateParenthesis(self, n):
        l=[]
        def backtrack(current, open_count, close_count):
            if open_count==n and close_count==n:
                l.append(current)
                return
            if open_count<n:
                backtrack(current+"(", open_count+1, close_count)
            if close_count<open_count:
                backtrack(current+")", open_count, close_count+1)
        backtrack('', 0, 0)
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna