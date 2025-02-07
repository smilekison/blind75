class Solution:
    def countSubstrings(self, s: str) -> int:
        def extend_palindrome(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total_count = 0
        for i in range(len(s)):
            # Count palindromes with odd length
            total_count += extend_palindrome(i, i)
            # Count palindromes with even length
            total_count += extend_palindrome(i, i + 1)

        return total_count



# https://leetcode.com/problems/palindromic-substrings/solutions/4705323/beats-100-users-easy-understood-solution-with-optimized-space-4-approaches