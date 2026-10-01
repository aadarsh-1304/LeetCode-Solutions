class Solution(object):
    def isValid(self, s):
        pairs={")":"(", "]":"[", "}":"{"}
        stack=[]
        for i in s:
            if i in pairs:
                if not stack or stack.pop()!=pairs[i]:
                    return False
            else:
                stack.append(i)
        return len(stack)==0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna