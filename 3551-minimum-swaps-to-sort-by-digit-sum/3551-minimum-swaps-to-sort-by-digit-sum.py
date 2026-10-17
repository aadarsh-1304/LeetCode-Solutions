class Solution(object):
    def minSwaps(self, nums):
        def digitSum(n):
            total=0
            while n>0:
                total+=n%10
                n//=10
            return total
        arr=sorted(nums, key=lambda x: (digitSum(x), x))
        pos={num: i for i, num in enumerate(nums)}
        swaps=0
        for i in range(len(nums)):
            if nums[i]!=arr[i]:
                j=pos[arr[i]]
                pos[nums[i]]=j
                pos[arr[i]]=i
                nums[i], nums[j]=nums[j], nums[i]
                swaps+=1
        return swaps

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna