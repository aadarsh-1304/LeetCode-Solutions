class Solution(object):
    def removeOuterParentheses(self, s):
        result='' ; count=0
        for i in s:
            if i=="(":
                if count>0:
                    result+=i
                count+=1
            else:
                count-=1
                if count>0:
                    result+=i
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna