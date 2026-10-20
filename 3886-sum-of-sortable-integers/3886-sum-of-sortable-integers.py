class Solution(object):
    def sortableIntegers(self, nums):
        n=len(nums) ; target=sorted(nums) ; ans=0
        def isRotation(a, b):
            k=len(a)
            arr=a+a
            lps=[0]*k
            j=0
            for i in range(1, k):
                while j>0 and b[i]!=b[j]:
                    j=lps[j-1]
                if b[i]==b[j]:
                    j+=1
                    lps[i]=j
            i=j=0
            while i<2*k-1:
                if arr[i]==b[j]:
                    i+=1
                    j+=1
                    if j==k:
                        return True
                elif j>0:
                    j=lps[j-1]
                else:
                    i+=1
            return False
        for k in range(1, n+1):
            if n%k!=0:
                continue
            ok=True
            for start in range(0, n, k):
                a=nums[start:start+k]
                b=target[start:start+k]
                if not isRotation(a, b):
                    ok=False
                    break
            if ok:
                ans+=k
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna