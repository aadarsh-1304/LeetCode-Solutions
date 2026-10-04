class Solution(object):
    def checkValidString(self, s):
        low=0 ; high=0
        for i in s:
            if i=="(":
                high+=1 ; low+=1
            elif i==")":
                high-=1 ; low-=1
            elif i=="*":
                high+=1 ; low-=1
            if high<0:
                return False
            low=max(low, 0)
        return low==0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna