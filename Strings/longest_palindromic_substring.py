# Problem: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Difficulty: Medium
# Topic: String, Two Pointer

# Approach:
# Expand around center to find longest palindrome substring

# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution(object):
    def longestPalindrome(self, s):

        def centre(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""

        for i in range(len(s)):
            odd = centre(s, i, i)
            even = centre(s, i, i+1)

            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result
