class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        seen = set()  # Initialize an empty set to track seen elements
        for num in nums:  # Iterate through the list
            if num in seen:  # If the element is already in the set, it's a duplicate
                return True
            seen.add(num)  # Add the element to the set
        return False  # No duplicates found

    print(containsDuplicate([1,2,3,4,1]))  # Test the function with an example

'''
SUMMARY
    Time Complexity: O(n).

    Space Complexity: O(n).

'''