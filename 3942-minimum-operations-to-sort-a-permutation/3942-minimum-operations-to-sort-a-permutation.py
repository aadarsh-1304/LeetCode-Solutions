class Solution(object):
    def minOperations(self, nums):
        n=len(nums)
        if nums==list(range(n)):
            return 0
        ans=float('inf') ; s=nums[0]
        if all(nums[i]==(i+s)%n for i in range(n)):
            ans=min(ans, min((n-s)%n, s+2))
        s=(n-1-nums[0])%n
        if all(nums[i]==(n-1-(i+s)%n) for i in range(n)):
            ans=min(ans, 1+min(s, n-s))
        return ans if ans!=float('inf') else -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna