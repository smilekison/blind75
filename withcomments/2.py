class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        newValue = {}  # Dictionary to store values and their indices

        for i, v in enumerate(nums):  # Loop through the list with index and value
            compliment = target - v  # Calculate the complement needed to reach the target
            if compliment in newValue:  # Check if the complement exists in the dictionary
                return [newValue[compliment], i]  # Return the indices of the complement and current value
            newValue[v] = i  # Store the current value and its index in the dictionary
        
        return []  # Return an empty list if no valid pair is found
    
    print(twoSum([2,7,11,15], 26))  # Test the function with an example



'''
Summary

    DSA Used: Hash Map (Dictionary) for efficient lookups.

    Time Complexity: O(n).

    Space Complexity: O(n).

'''