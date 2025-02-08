class Solution:
    def numDecodings(self, s: str) -> int:
        str_len = len(s)

        dp = [0] * (str_len + 1)
        # there is only one way to decode an empty string
        dp[0] = 1

        # the first element of the dp array is 1 if the first
        # character of the string is not '0',
        if s[0] != "0":
            dp[1] = 1
        else:
            # there's no way to decode a string that starts
            # with '0'
            return 0

        # iterate through the input string starting from the
        # 2nd character
        for i in range(2, str_len + 1):
            # if the current character is not '0', add the
            # number of ways to decode the substring without
            # the current character
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            # if the substring of the current and previous
            # characters is a valid two-digit number, add the
            # number of ways to decode the substring without
            # the current and previous characters
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]

        return dp[str_len]



# https://leetcode.com/problems/decode-ways/solutions/6059932/simple-solution-with-diagrams-in-video-javascript-c-java-python