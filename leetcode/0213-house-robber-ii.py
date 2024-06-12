class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n==2:
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        first_no_last = dp[n-2]
        
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        last_no_first = dp[n-1]
        return max(first_no_last, last_no_first)