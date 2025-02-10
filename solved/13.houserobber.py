class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1] 
    

#    https://leetcode.com/problems/house-robber/solutions/6147042/2-solutions-o-n-space-and-o-1-space 