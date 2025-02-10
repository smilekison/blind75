class Solution:
    def wordBreak(s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n +1)
        dp[n] = True

        for i in range(n -1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= n and s[i: i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
        
    print(wordBreak("leetcode", ["leet","code"]))
    print(wordBreak("catsandog", ["cats","and","og"]))
    print(wordBreak("applepenapple", ["apple","pen"]))