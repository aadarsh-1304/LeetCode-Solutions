class Solution(object):
    def minOperations(self, s):
        if s==''.join(sorted(s)):
            return 0
        n=len(s)
        if n==2:
            return -1
        mn=min(s)
        mx=max(s)
        if s[0]==mn or s[-1]==mx:
            return 1
        if mn in s[1:-1] or mx in s[1:-1]:
            return 2
        return 3

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna