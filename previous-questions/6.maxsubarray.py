class Solution:
    def maxSubArray(nums: list[int]) -> int:
        maxV = nums[0]
        curSum = 0

        for v in nums:
            if curSum < 0:
                curSum = 0
            curSum += v

        maxV = max(maxV, curSum)
        return maxV
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))