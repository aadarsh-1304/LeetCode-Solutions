class Solution(object):
    def sumCounts(self, nums):
        MOD=10**9+7
        n=len(nums)
        tree_sum=[0]*(4*n)
        tree_sq=[0]*(4*n)
        lazy=[0]*(4*n)
        def update(node, start, end, left, right):
            if left<=start and end<=right:
                length=end-start+1
                tree_sq[node]=(tree_sq[node]+2*lazy_add*tree_sum[node]+length*lazy_add*lazy_add)%MOD
                tree_sum[node]=(tree_sum[node]+length*lazy_add)%MOD
                lazy[node]=(lazy[node]+lazy_add)%MOD
                return
            mid=(start+end)//2
            push(node, start, end)
            if left<=mid:
                update(node*2, start, mid, left, right)
            if right>mid:
                update(node*2+1, mid+1, end, left, right)
            tree_sum[node]=(tree_sum[node*2]+tree_sum[node*2+1])%MOD
            tree_sq[node]=(tree_sq[node*2]+tree_sq[node*2+1])%MOD
        def push(node, start, end):
            if lazy[node]==0 or start==end:
                return
            value=lazy[node]
            mid=(start+end)//2
            for child, length in ((node*2, mid-start+1), (node*2+1, end-mid)):
                tree_sq[child]=(tree_sq[child]+2*value*tree_sum[child]+length*value*value)%MOD
                tree_sum[child]=(tree_sum[child]+length*value)%MOD
                lazy[child]=(lazy[child]+value)%MOD
            lazy[node]=0
        last={} ; ans=0
        for i, x in enumerate(nums):
            left=last.get(x, -1)+1
            lazy_add=1
            update(1, 0, n-1, left, i)
            last[x]=i
            ans=(ans+tree_sq[1])%MOD
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna