class Solution(object):
    def shuffle(self, nums, n):
        arr=[]
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna