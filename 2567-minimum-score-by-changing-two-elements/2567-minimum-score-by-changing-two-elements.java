class Solution {
    public int minimizeSum(int[] nums) {
        int n=nums.length;
        Arrays.sort(nums);
        return Math.min(nums[n-1]-nums[2], Math.min(nums[n-2]-nums[1], nums[n-3]-nums[0]));
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna