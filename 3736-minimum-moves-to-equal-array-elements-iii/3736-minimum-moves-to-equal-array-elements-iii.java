class Solution {
    public int minMoves(int[] nums) {
        int m=nums[0], s=0;
        for (int i: nums){
            m=Math.max(m, i);
        }
        for (int i: nums){
            s+=m-i;
        }
        return s;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna