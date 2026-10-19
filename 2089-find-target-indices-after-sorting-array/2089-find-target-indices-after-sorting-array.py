class Solution(object):
    def targetIndices(self, nums, target):
        pos=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                pos.append(i)
        return pos

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna