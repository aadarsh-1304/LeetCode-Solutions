class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum>9*num:
            return ""
        result=""
        while num>0:
            digit=min(9, sum)
            result+=str(digit)
            sum-=digit
            num-=1
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna