class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0; Max=0
        for i in nums:
            if i==1:
                count+=1
                Max=max(Max, count)
            else:
                count=0
        return Max      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna