from collections import defaultdict  # Import defaultdict to simplify dictionary operations

class Solution:
    def groupAnagrams(strs: list[str]) -> list[list[str]]:  # Method to group anagrams together
        res = defaultdict(list)  # Initialize a defaultdict to store groups of anagrams
        
        for s in strs:  # Iterate through each string in the input list
            count = [0] * 26  # Initialize a list to count the frequency of each letter in the string
            for c in s:  # Iterate through each character in the string
                count[ord(c) - ord("a")] += 1  # Increment the count for the corresponding letter
            
            # Use the tuple of the count list as a key in the dictionary
            # Anagrams will have the same tuple representation
            res[tuple(count)].append(s)  # Append the string to the corresponding group

        return res.values()  # Return the grouped anagrams as a list of lists

    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # Test the function with an example


'''
Summary

    DSA Used: Hash Map (Dictionary) with Frequency Count.

    Time Complexity: O(n * k).

    Space Complexity: O(n * k).

'''