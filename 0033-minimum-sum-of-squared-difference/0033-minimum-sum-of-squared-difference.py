class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k=k1+k2
        diff=[abs(a-b) for a, b in zip(nums1, nums2)]
        if sum(diff)<=k:
            return 0
        left, right=0, max(diff)
        while left<right:
            mid=(left+right)//2
            need=sum(max(0, d-mid) for d in diff)
            if need<=k:
                right=mid
            else:
                left=mid+1
        diff=[min(d, left) for d in diff]
        remaining=k-sum(
            max(0, d-left) for d in [abs(a-b) for a, b in zip(nums1, nums2)]
        )
        diff.sort(reverse=True)
        for i in range(remaining):
            if diff[i]>0:
                diff[i]-=1
        return sum(d*d for d in diff)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna