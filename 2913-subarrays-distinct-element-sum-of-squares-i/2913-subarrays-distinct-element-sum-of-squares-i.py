class Solution(object):
    def sumCounts(self, nums):
        ans=0
        for i in range(len(nums)):
            s=set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                ans+=len(s)*len(s)
        return ans    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna