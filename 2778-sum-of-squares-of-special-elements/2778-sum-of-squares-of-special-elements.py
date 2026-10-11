class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums) ; s=0
        for i in range(1, n+1):
            if n%i==0:
                s+=nums[i-1]*nums[i-1]
        return s

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna