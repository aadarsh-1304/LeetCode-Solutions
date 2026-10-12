class Solution(object):
    def maxSum(self, nums, k):
        MOD=10**9+7 ; count=[0]*32 ; ans=0
        for num in nums:
            for bit in range(32):
                if num & (1<<bit):
                    count[bit]+=1
        for j in range(k):
            num=0
            for bit in range(32):
                if count[bit]>0:
                    num|=(1<<bit)
                    count[bit]-=1
            ans=(ans+num*num)%MOD
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna