class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:  # Method to find the length of the longest increasing subsequence
        res = []  # Initialize a list to store the smallest tail values of all increasing subsequences

        def binary_search(res, n):  # Binary search to find the position to replace or insert `n`
            left = 0
            right = len(res) - 1

            while left <= right:  # Perform binary search
                mid = (left + right) // 2
                if res[mid] == n:  # If `n` is found, return its index
                    return mid
                elif res[mid] > n:  # If `n` is smaller, search the left half
                    right = mid - 1
                else:  # If `n` is larger, search the right half
                    left = mid + 1
            
            return left  # Return the position to insert `n`

        for n in nums:  # Iterate through each number in the input list
            if not res or res[-1] < n:  # If `res` is empty or the last element is smaller than `n`, append `n`
                res.append(n)
            else:  # Otherwise, find the position to replace or insert `n` using binary search
                idx = binary_search(res, n)
                res[idx] = n  # Replace the element at `idx` with `n`
        
        return len(res)  # Return the length of `res`, which represents the length of the longest increasing subsequence

'''
Summary

    DSA Used: Binary Search, Greedy Algorithm.

    Time Complexity: O(n log n).

    Space Complexity: O(n).

'''