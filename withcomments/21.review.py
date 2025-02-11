class Solution:
    def wordBreak(s: str, wordDict: list[str]) -> bool:  # Method to check if the string can be segmented into words from the dictionary
        n = len(s)  # Length of the string
        dp = [False] * (n + 1)  # Initialize a DP array to store whether the substring s[i:n] can be segmented
        dp[n] = True  # Base case: an empty string can always be segmented

        for i in range(n - 1, -1, -1):  # Iterate through the string from the end to the start
            print(wordDict)
            for w in wordDict:  # Iterate through each word in the dictionary
                # Check if the current word matches the substring starting at index i
                if (i + len(w)) <= n and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]  # Update dp[i] based on dp[i + len(w)]
                if dp[i]:  # If dp[i] is True, no need to check further words
                    break

        # return dp[0]  # Return whether the entire string can be segmented

    # Test cases
    print(wordBreak("leetcode", ["leet", "code"]))  # True
    # print(wordBreak("catsandog", ["cats", "and", "og"]))  # False
    # print(wordBreak("applepenapple", ["apple", "pen"]))  # True


'''
Summary

    DSA Used: Dynamic Programming (DP).

    Time Complexity: O(n * m * k).

    Space Complexity: O(n).

'''