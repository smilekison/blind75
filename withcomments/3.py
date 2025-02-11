class Solution:
    def containsDuplicate(nums: list[int]) -> bool:  # Method to check if the list contains duplicate values
        newValue = set(nums)  # Convert the list to a set to remove duplicates

        if len(nums) == len(newValue):  # Compare the length of the list and the set
            return False  # If lengths are equal, no duplicates exist
        return True  # If lengths are not equal, duplicates exist

    print(containsDuplicate([1,2,3,4,1]))  # Test the function with an example


'''
Summary

    DSA Used: Set for storing unique values.

    Time Complexity: O(n).

    Space Complexity: O(n).

'''