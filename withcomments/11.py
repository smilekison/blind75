class Solution:
    def maxSubArray(nums: list[int]) -> int:  # Method to find the maximum sum of a contiguous subarray
        maxV = nums[0]  # Initialize maxV to the first element of the array
        curSum = 0  # Initialize curSum to 0 to track the current subarray sum

        for v in nums:  # Iterate through each element in the array
            if curSum < 0:  # If the current subarray sum is negative, reset it to 0
                curSum = 0
            curSum += v  # Add the current element to the current subarray sum
            maxV = max(maxV, curSum)  # Update maxV with the maximum of itself and curSum

        return maxV  # Return the maximum subarray sum

    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Test the function with an example


'''
Summary

    DSA Used: Kadane’s Algorithm.

    Time Complexity: O(n).

    Space Complexity: O(1).

'''