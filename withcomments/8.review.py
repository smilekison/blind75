class Solution:
    def characterReplacement(self, s: str, k: int) -> int:  # Method to find the length of the longest substring with at most k replacements
        hasho = {}  # Dictionary to store the frequency of characters in the current window
        most_frequent = 0  # Track the frequency of the most frequent character in the window
        start = 0  # Start index of the sliding window
        max_len = 0  # Track the maximum length of the valid substring

        for end, char in enumerate(s):  # Iterate through the string with end as the end index of the window
            # Update the frequency of the current character in the dictionary
            hasho[char] = hasho.get(char, 0) + 1
            
            # Update the frequency of the most frequent character in the current window
            most_frequent = max(most_frequent, hasho[char])
            
            # Calculate the number of replacements needed in the current window
            # (end - start + 1) is the size of the current window
            # (end - start + 1) - most_frequent is the number of characters that need to be replaced
            if (end - start + 1) - most_frequent > k:
                # If replacements needed exceed k, move the start of the window to the right
                hasho[s[start]] -= 1  # Decrease the frequency of the character at the start of the window
                start += 1  # Move the start of the window to the right
            
            # Update the maximum length of the valid substring
            max_len = max(max_len, end - start + 1)
        
        return max_len  # Return the maximum length of the valid substring
    

'''
Summary

    DSA Used: Sliding Window with Hash Map.

    Time Complexity: O(n).

    Space Complexity: O(1).

'''