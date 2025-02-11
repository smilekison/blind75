class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:  # Method to find all unique triplets that sum to zero
        res = []  # Initialize the result list to store valid triplets
        nums.sort()  # Sort the input list to enable the two-pointer approach

        for i in range(len(nums)):  # Iterate through the list
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values for the first element
                continue

            j = i + 1  # Initialize the second pointer (left pointer)
            k = len(nums) - 1  # Initialize the third pointer (right pointer)

            while j < k:  # Use the two-pointer approach to find valid triplets
                total = nums[i] + nums[j] + nums[k]  # Calculate the sum of the current triplet

                if total > 0:  # If the sum is too large, move the right pointer left
                    k -= 1
                elif total < 0:  # If the sum is too small, move the left pointer right
                    j += 1
                else:  # If the sum is zero, we found a valid triplet
                    res.append([nums[i], nums[j], nums[k]])  # Add the triplet to the result list
                    j += 1  # Move the left pointer to the right

                    while nums[j] == nums[j - 1] and j < k:  # Skip duplicate values for the second element
                        j += 1

        return res  # Return the list of valid triplets
    

'''
Summary

    DSA Used: Sorting, Two-Pointer Technique.

    Time Complexity: O(n^2).

    Space Complexity: O(n) (due to the output list).

'''