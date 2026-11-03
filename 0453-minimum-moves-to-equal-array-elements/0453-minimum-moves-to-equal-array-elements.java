class Solution {
    public int minMoves(int[] nums) {
        int sum=0, min=nums[0];
        for (int num: nums){
            min=Math.min(min, num);
            sum+=num;
        }
        return sum-nums.length*min;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna