class Solution(object):
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            balance=0
            for char in string:
                if char=='(':
                    balance+=1
                elif char==')':
                    balance-=1
                    if balance<0:
                        return False
            return balance==0
        queue={s}
        while queue:
            valid=[]
            for string in queue:
                if is_valid(string):
                    valid.append(string)
            if valid:
                return valid
            next_level=set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i]+string[i+1:])
            queue=next_level

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna