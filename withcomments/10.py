class Solution:
    def lengthOfLongestSubstring(s: str) -> int:  # Method to find the length of the longest substring without repeating characters
        n = len(s)  # Length of the input string
        maxLength = 0  # Variable to store the maximum length of the substring
        charSet = set()  # Set to store unique characters in the current window
        left = 0  # Left pointer of the sliding window

        for right in range(n):  # Iterate through the string with the right pointer
            print(right, s[right])
            if s[right] not in charSet:  # If the current character is not in the set
                charSet.add(s[right])  # Add it to the set
                # print(right - left)
                maxLength = max(maxLength, right - left + 1)  # Update the maximum length
            else:  # If the current character is already in the set (repeating character)
                while s[right] in charSet:  # Move the left pointer to the right until the repeating character is removed
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])  # Add the current character to the set
        
        # return maxLength  # Return the maximum length found
    
    print(lengthOfLongestSubstring("hello"))
'''
Summary

    DSA Used: Sliding Window with Set.

    Time Complexity: O(n).

    Space Complexity: O(min(n, m)).

'''