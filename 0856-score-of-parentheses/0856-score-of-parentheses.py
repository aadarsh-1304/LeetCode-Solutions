class Solution(object):
    def scoreOfParentheses(self, s):
        stack=[0]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(0)
            else:
                current=stack.pop()
                if current==0:
                    score=1
                else:
                    score=2*current
                stack[-1]+=score
        return stack[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna