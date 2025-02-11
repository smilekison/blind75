class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:  # Method to compute the product of the array except self
        res = [1] * len(nums)  # Initialize the result array with 1s

        prefix = 1  # Initialize prefix product
        for i in range(len(nums)):  # Traverse the array from left to right
            res[i] = prefix  # Store the prefix product up to the current index
            prefix *= nums[i]  # Update the prefix product

        postfix = 1  # Initialize postfix product
        for i in range(len(nums) - 1, -1, -1):  # Traverse the array from right to left
            res[i] *= postfix  # Multiply the postfix product with the prefix product stored in res[i]
            postfix *= nums[i]  # Update the postfix product

        return res  # Return the final result array

    print(productExceptSelf([-1, 1, 0, -3, 3]))  # Test the function with an example


'''
Summary

    DSA Used: Prefix and Postfix Product Calculation.

    Time Complexity: O(n).

    Space Complexity: O(n).

'''