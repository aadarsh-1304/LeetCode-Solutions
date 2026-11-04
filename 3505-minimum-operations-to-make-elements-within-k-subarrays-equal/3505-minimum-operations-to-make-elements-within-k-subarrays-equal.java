class Solution {
    TreeMap<Integer, Integer> left=new TreeMap<>();
    TreeMap<Integer, Integer> right=new TreeMap<>();
    long sumLeft=0;
    long sumRight=0;
    int sizeLeft=0;
    int sizeRight=0;
    public long minOperations(int[] nums, int x, int k) {
        int n=nums.length;
        long[] cost=new long[n-x+1];
        for (int i=0; i<x; i++){
            add(nums[i]);
        }
        cost[0]=getCost();
        for (int i=x; i<n; i++){
            remove(nums[i-x]);
            add(nums[i]);
            cost[i-x+1]=getCost();
        }
        long INF=Long.MAX_VALUE/2;
        long[][] dp=new long[k+1][n+1];
        for (int i=0; i<=k; i++){
            Arrays.fill(dp[i], INF);
        }
        for (int i=0; i<=n; i++){
            dp[0][i]=0;
        }
        for (int j=1; j<=k; j++){
            for (int i=1; i<=n; i++){
                dp[j][i]=dp[j][i-1];
                if (i>=x && dp[j-1][i-x]!=INF){
                    dp[j][i]=Math.min(dp[j][i], dp[j-1][i-x]+cost[i-x]);
                }
            }
        }
        return dp[k][n];
    }

    void add(int num) {
        int target=(sizeLeft+sizeRight+1)/2;
        if (sizeLeft==0 || num<=left.lastKey()){
            left.put(num, left.getOrDefault(num, 0)+1);
            sizeLeft++;
            sumLeft+=num;
        }
        else{
            right.put(num, right.getOrDefault(num, 0)+1);
            sizeRight++;
            sumRight+=num;
        }
        balance();
    }

    void remove(int num) {
        if (left.containsKey(num)){
            removeValue(left, num);
            sizeLeft--;
            sumLeft-=num;
        }
        else{
            removeValue(right, num);
            sizeRight--;
            sumRight-=num;
        }
        balance();
    }

    void balance() {
        int target=(sizeLeft+sizeRight+1)/2;
        while (sizeLeft>target){
            int num=left.lastKey();
            removeValue(left, num);
            sizeLeft--;
            sumLeft-=num;
            right.put(num, right.getOrDefault(num, 0)+1);
            sizeRight++;
            sumRight+=num;
        }
        while (sizeLeft<target){
            int num=right.firstKey();
            removeValue(right, num);
            sizeRight--;
            sumRight-=num;
            left.put(num, left.getOrDefault(num, 0)+1);
            sizeLeft++;
            sumLeft+=num;
        }
    }

    void removeValue(TreeMap<Integer, Integer> map, int num) {
        int count=map.get(num);
        if (count==1){
            map.remove(num);
        }
        else{
            map.put(num, count-1);
        }
    }

    long getCost() {
        int median=left.lastKey();
        return (long) median*sizeLeft-sumLeft+sumRight-(long) median*sizeRight;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna