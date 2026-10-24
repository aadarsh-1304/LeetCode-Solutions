class Solution(object):
    def sortPermutation(self, nums):
        n=len(nums) ; k=-1
        for i in range(n):
            if nums[i]!=i:
                k&=nums[i]&i
        return max(0, k)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna