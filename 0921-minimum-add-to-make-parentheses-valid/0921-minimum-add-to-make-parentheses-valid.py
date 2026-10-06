class Solution(object):
    def minAddToMakeValid(self, s):
        b=0 ; a=0
        for i in s:
            if i=="(":
                b+=1
            else:
                if b>0:
                    b-=1
                else:
                    a+=1
        return a+b        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna